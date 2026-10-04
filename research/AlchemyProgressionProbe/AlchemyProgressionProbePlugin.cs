// SPDX-License-Identifier: MPL-2.0
using BepInEx;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Reflection;
using System.Text.RegularExpressions;
using UnityEngine;

namespace NikichMods.AlchemyRiddle.Research
{
    [BepInPlugin(Guid, Name, Version)]
    public sealed class AlchemyProgressionProbePlugin : BaseUnityPlugin
    {
        public const string Guid = "nikich.graveyardkeeper.alchemyriddle.progressionprobe";
        public const string Name = "AlchemyRiddle Progression Probe";
        public const string Version = "0.1.1";

        private static readonly BindingFlags Inst =
            BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic;
        private static readonly BindingFlags Stat =
            BindingFlags.Static | BindingFlags.Public | BindingFlags.NonPublic;

        private static readonly string[] FocusTerms =
        {
            "merchant_curse",
            "taste_booster:alchemy_1_spice",
            "alchemy_1_spice",
            "pot_heal",
            "alchemy_1_yellow",
            "The Beginning Of Alchemy",
            "UnlockAlchemy",
            "UnlockRandomAlchemy",
            "clotho",
            "сlotho"
        };

        private Assembly _gameAssembly;
        private Type _gjlType;
        private MethodInfo _localize;
        private bool _dumped;

        private sealed class Node
        {
            internal string Id;
            internal string Type;
            internal int TypePosition;
            internal string Uid;
            internal string SourceOutputUid;
        }

        private sealed class Connection
        {
            internal string SourcePort;
            internal string TargetPort;
            internal string SourceNode;
            internal string TargetNode;
        }

        private void Awake()
        {
            Logger.LogInfo("AlchemyRiddle Progression Probe 0.1.1 loaded. Read-only progression/FlowCanvas research probe.");
            StartCoroutine(DumpWhenReady());
        }

        private IEnumerator DumpWhenReady()
        {
            while (!_dumped)
            {
                if (BindGame())
                {
                    Type mainGame = FindType("MainGame");
                    Type balanceType = FindType("GameBalance");
                    if (Bool(GetStatic(mainGame, "game_started")))
                    {
                        object balance = GetStatic(balanceType, "me");
                        if (balance != null)
                        {
                            for (int i = 0; i < 120; i++)
                                yield return null;

                            try
                            {
                                InitLocalization();
                                Dump(balance);
                            }
                            catch (Exception ex)
                            {
                                Logger.LogError("AR_PROGRESSION_ERROR|" + Esc(ex.ToString()));
                            }

                            _dumped = true;
                            yield break;
                        }
                    }
                }

                yield return null;
            }
        }

        private void Dump(object balance)
        {
            IList items = Get(balance, "items_data") as IList;
            IList crafts = Get(balance, "craft_data") as IList;
            IList techs = Get(balance, "techs_data") as IList;
            if (items == null || crafts == null || techs == null)
                throw new InvalidOperationException("GameBalance items_data/craft_data/techs_data not available.");

            Dictionary<string, object> itemById = IndexById(items);
            Dictionary<string, object> craftById = IndexById(crafts);
            Dictionary<string, object> techById = IndexById(techs);

            Logger.LogInfo("AR_PROGRESSION_BEGIN|probe=0.1.1|target=GraveyardKeeper-1.407|source=loaded-GameBalance+loaded-FlowCanvas");
            Logger.LogInfo("AR_PROGRESSION_SOURCE|flow_parser_lineage=NikichMods/DayWheelQuestMarkers-1.1.14|decompile_reference=Kupie/GYK_DECOMP@6abf79199d92482af1c7573870dd9a20ec2270b9");
            Logger.LogInfo("AR_PROGRESSION_POLICY|read_only=true|formula_rows_logged=0|exact_formula_ids_logged=0");

            DumpTechAnchor(techById, "The Beginning Of Alchemy");
            DumpTechAnchor(techById, "Alchemy storage");
            DumpTechAnchor(techById, "Advanced alchemy");
            DumpTechAnchor(techById, "Embalm 1");
            DumpTechAnchor(techById, "Embalm 2");

            int itemUnlocks = DumpItemDisclosureChannels(items, craftById, itemById);

            Type controllerType = FindType("FlowCanvas.FlowScriptController");
            if (controllerType == null)
                throw new InvalidOperationException("FlowCanvas.FlowScriptController type not found.");

            UnityEngine.Object[] controllers = Resources.FindObjectsOfTypeAll(controllerType);
            int graphCount = 0;
            int unlockRows = 0;
            int randomRows = 0;
            int focusGraphs = 0;
            int techUnlockRows = 0;
            int craftUnlockRows = 0;
            int clothoAnswerRows = 0;
            var seenGraphs = new HashSet<string>(StringComparer.Ordinal);

            foreach (UnityEngine.Object rawController in controllers)
            {
                object controller = rawController;
                if (controller == null)
                    continue;

                object graph = Get(controller, "_graph");
                object serializedValue = Get(graph, "_serializedGraph");
                string serialized = serializedValue as string;
                if (string.IsNullOrEmpty(serialized))
                    continue;

                string graphName = GraphName(rawController, graph);
                string dedupe = graphName + "\n" + serialized.Length.ToString(CultureInfo.InvariantCulture) + "\n" +
                                (serialized.Length <= 96 ? serialized : serialized.Substring(0, 96));
                if (!seenGraphs.Add(dedupe))
                    continue;

                graphCount++;
                Dictionary<string, Node> nodes = BuildNodeIndex(serialized);
                List<Connection> connections = ParseConnections(serialized);

                unlockRows += DumpUnlockOccurrences(
                    graphName, serialized, nodes, craftById, itemById, "UnlockAlchemy", false);
                randomRows += DumpUnlockOccurrences(
                    graphName, serialized, nodes, craftById, itemById, "UnlockRandomAlchemy", true);
                techUnlockRows += DumpUnlockTechNodes(
                    graphName, serialized, nodes, techById, craftById, itemById);
                craftUnlockRows += DumpUnlockCraftNodes(
                    graphName, serialized, nodes, craftById, itemById);
                if (graphName.IndexOf("npc_witch", StringComparison.OrdinalIgnoreCase) >= 0)
                    clothoAnswerRows += DumpClothoAnswerData(
                        graphName, serialized, nodes, connections, itemById);

                if (IsFocusGraph(graphName, serialized))
                {
                    focusGraphs++;
                    DumpFocusGraph(graphName, serialized, nodes, connections);
                }
            }

            Logger.LogInfo(
                "AR_PROGRESSION_SUMMARY" +
                "|controllers_seen=" + controllers.Length.ToString(CultureInfo.InvariantCulture) +
                "|unique_graphs=" + graphCount.ToString(CultureInfo.InvariantCulture) +
                "|scripted_unlock_rows=" + unlockRows.ToString(CultureInfo.InvariantCulture) +
                "|random_unlock_rows=" + randomRows.ToString(CultureInfo.InvariantCulture) +
                "|item_unlock_rows=" + itemUnlocks.ToString(CultureInfo.InvariantCulture) +
                "|tech_unlock_rows=" + techUnlockRows.ToString(CultureInfo.InvariantCulture) +
                "|craft_unlock_rows=" + craftUnlockRows.ToString(CultureInfo.InvariantCulture) +
                "|clotho_answer_rows=" + clothoAnswerRows.ToString(CultureInfo.InvariantCulture) +
                "|focus_graphs=" + focusGraphs.ToString(CultureInfo.InvariantCulture) +
                "|formula_rows_logged=0");

            Logger.LogInfo("AR_PROGRESSION_DONE|probe=0.1.1|formula_rows_logged=0");
        }


        private int DumpUnlockTechNodes(
            string graphName,
            string serialized,
            Dictionary<string, Node> nodes,
            Dictionary<string, object> techById,
            Dictionary<string, object> craftById,
            Dictionary<string, object> itemById)
        {
            int rows = 0;
            foreach (Node node in nodes.Values)
            {
                if (!node.Type.EndsWith("Flow_UnlockTech", StringComparison.Ordinal))
                    continue;

                string techId =
                    ReadNodeContent(serialized, node, "tech id") ??
                    ReadNodeContent(serialized, node, "Tech id") ??
                    ReadNodeContent(serialized, node, "tech_id") ??
                    string.Empty;

                bool silent;
                bool showTech;
                TryReadNodeBool(serialized, node, "silent?", out silent);
                TryReadNodeBool(serialized, node, "show tech", out showTech);

                object tech;
                bool resolved = techById.TryGetValue(techId, out tech) && tech != null;
                var targets = new List<string>();

                if (resolved)
                {
                    IList craftIds = Get(tech, "crafts") as IList;
                    if (craftIds != null)
                    {
                        foreach (object raw in craftIds)
                        {
                            string craftId = Str(raw);
                            object craft;
                            if (!craftById.TryGetValue(craftId, out craft) || craft == null)
                                continue;
                            if (!IsSuccessFormula(craft) || !IsPickerCompatible(craft, itemById))
                                continue;

                            string targetId = PrimaryOutput(craft);
                            object targetDef;
                            itemById.TryGetValue(targetId, out targetDef);
                            string targetName = targetDef == null ? Localize(targetId) : ItemName(targetDef);
                            int arity = ItemIds(Get(craft, "needs") as IList).Count();
                            targets.Add(targetName + "~" + arity.ToString(CultureInfo.InvariantCulture));
                        }
                    }
                }

                Logger.LogInfo(
                    "AR_PROGRESSION_TECH_UNLOCK" +
                    "|graph=" + Esc(graphName) +
                    "|node=" + Esc(node.Id) +
                    "|tech_id=" + Esc(techId) +
                    "|tech_name=" + Esc(Localize(techId)) +
                    "|resolved=" + resolved.ToString().ToLowerInvariant() +
                    "|silent=" + silent.ToString().ToLowerInvariant() +
                    "|show_tech=" + showTech.ToString().ToLowerInvariant() +
                    "|ordinary_mixed_targets=" + Esc(string.Join(";", targets.Distinct().ToArray())));
                rows++;
            }

            return rows;
        }

        private int DumpUnlockCraftNodes(
            string graphName,
            string serialized,
            Dictionary<string, Node> nodes,
            Dictionary<string, object> craftById,
            Dictionary<string, object> itemById)
        {
            int rows = 0;
            foreach (Node node in nodes.Values)
            {
                if (!node.Type.EndsWith("Flow_UnlockCraft", StringComparison.Ordinal))
                    continue;

                string craftId =
                    ReadNodeContent(serialized, node, "Craft id") ??
                    ReadNodeContent(serialized, node, "craft id") ??
                    string.Empty;

                object craft;
                bool resolved = craftById.TryGetValue(craftId, out craft) && craft != null;
                bool ordinary = resolved && IsSuccessFormula(craft) && IsPickerCompatible(craft, itemById);

                string targetName = string.Empty;
                int arity = 0;
                if (ordinary)
                {
                    string targetId = PrimaryOutput(craft);
                    object targetDef;
                    itemById.TryGetValue(targetId, out targetDef);
                    targetName = targetDef == null ? Localize(targetId) : ItemName(targetDef);
                    arity = ItemIds(Get(craft, "needs") as IList).Count();
                }

                Logger.LogInfo(
                    "AR_PROGRESSION_CRAFT_UNLOCK" +
                    "|graph=" + Esc(graphName) +
                    "|node=" + Esc(node.Id) +
                    "|resolved=" + resolved.ToString().ToLowerInvariant() +
                    "|ordinary_mixed=" + ordinary.ToString().ToLowerInvariant() +
                    "|target=" + Esc(targetName) +
                    "|arity=" + arity.ToString(CultureInfo.InvariantCulture));
                rows++;
            }

            return rows;
        }

        private int DumpClothoAnswerData(
            string graphName,
            string serialized,
            Dictionary<string, Node> nodes,
            List<Connection> connections,
            Dictionary<string, object> itemById)
        {
            int rows = 0;
            foreach (Node multi in nodes.Values)
            {
                if (!multi.Type.EndsWith("Flow_MultiAnswer", StringComparison.Ordinal))
                    continue;

                List<string> answers = ReadMultiAnswers(serialized, multi);
                bool relevant = answers.Any(delegate(string a)
                {
                    return a == "сlotho_vat" ||
                           a == "сlotho_pot" ||
                           a == "@сlotho_intence" ||
                           a == "@сlotho_bee" ||
                           a == "сlotho_need_help" ||
                           a == "@clotho_give_food" ||
                           a == "@сlotho_merch" ||
                           a == "@сlotho_merch_again";
                });
                if (!relevant)
                    continue;

                foreach (Connection answerLink in connections)
                {
                    if (answerLink.TargetNode != multi.Id)
                        continue;

                    int answerIndex = ParseAnswerPortIndex(answerLink.TargetPort);
                    if (answerIndex < 0 || answerIndex >= answers.Count)
                        continue;

                    Node answerNode;
                    if (!nodes.TryGetValue(answerLink.SourceNode, out answerNode) ||
                        answerNode.Type.IndexOf("Flow_Answer", StringComparison.Ordinal) < 0)
                        continue;

                    string price = string.Empty;
                    string gate = string.Empty;
                    string reward = string.Empty;

                    foreach (Connection valueLink in connections)
                    {
                        if (valueLink.TargetNode != answerNode.Id)
                            continue;

                        Node smartRes;
                        if (!nodes.TryGetValue(valueLink.SourceNode, out smartRes) ||
                            smartRes.Type.IndexOf("Flow_SmartRes", StringComparison.Ordinal) < 0)
                            continue;

                        string summary = DescribeSmartRes(serialized, smartRes, itemById);
                        if (string.Equals(valueLink.TargetPort, "price", StringComparison.OrdinalIgnoreCase))
                            price = summary;
                        else if (string.Equals(valueLink.TargetPort, "lock", StringComparison.OrdinalIgnoreCase))
                            gate = summary;
                        else if (string.Equals(valueLink.TargetPort, "reward", StringComparison.OrdinalIgnoreCase))
                            reward = summary;
                    }

                    Logger.LogInfo(
                        "AR_PROGRESSION_CLOTHO_ANSWER" +
                        "|graph=" + Esc(graphName) +
                        "|multi=" + Esc(multi.Id) +
                        "|index=" + answerIndex.ToString(CultureInfo.InvariantCulture) +
                        "|answer=" + Esc(answers[answerIndex]) +
                        "|price=" + Esc(price) +
                        "|lock=" + Esc(gate) +
                        "|reward=" + Esc(reward));
                    rows++;
                }
            }

            return rows;
        }

        private string DescribeSmartRes(
            string serialized,
            Node node,
            Dictionary<string, object> itemById)
        {
            string type =
                ReadNodeContent(serialized, node, "res_type") ??
                ReadNodeContent(serialized, node, "Res type") ??
                string.Empty;
            string id =
                ReadNodeContent(serialized, node, "id") ??
                ReadNodeContent(serialized, node, "Id") ??
                string.Empty;
            float value;
            bool hasValue = TryReadNodeNumber(serialized, node, "v", out value) ||
                            TryReadNodeNumber(serialized, node, "V", out value);

            object itemDef;
            string name = itemById.TryGetValue(id, out itemDef) && itemDef != null
                ? ItemName(itemDef)
                : Localize(id);

            return type + ":" + id + ":" + name + ":" +
                   (hasValue ? value.ToString("0.###", CultureInfo.InvariantCulture) : "?");
        }

        private static int ParseAnswerPortIndex(string port)
        {
            if (string.IsNullOrEmpty(port))
                return -1;

            int hash = port.LastIndexOf('#');
            if (hash < 0 || hash + 1 >= port.Length)
                return -1;

            int i = hash + 1;
            int value = 0;
            int digits = 0;
            while (i < port.Length && char.IsDigit(port[i]))
            {
                value = value * 10 + (port[i] - '0');
                digits++;
                i++;
            }

            return digits == 0 ? -1 : value;
        }

        private static bool TryReadNodeBool(string serialized, Node node, string key, out bool value)
        {
            value = false;
            if (node == null)
                return false;

            string window = NodeWindow(serialized, node, 3000);
            string marker = "\"" + key + "\":{\"$content\":";
            int pos = window.LastIndexOf(marker, StringComparison.Ordinal);
            if (pos < 0)
                return false;

            pos += marker.Length;
            while (pos < window.Length && char.IsWhiteSpace(window[pos]))
                pos++;

            if (window.IndexOf("true", pos, StringComparison.Ordinal) == pos)
            {
                value = true;
                return true;
            }
            if (window.IndexOf("false", pos, StringComparison.Ordinal) == pos)
            {
                value = false;
                return true;
            }

            return false;
        }

        private static bool TryReadNodeNumber(
            string serialized,
            Node node,
            string key,
            out float value)
        {
            value = 0f;
            if (node == null)
                return false;

            string window = NodeWindow(serialized, node, 3000);
            string marker = "\"" + key + "\":{\"$content\":";
            int pos = window.LastIndexOf(marker, StringComparison.Ordinal);
            if (pos < 0)
                return false;

            pos += marker.Length;
            while (pos < window.Length && char.IsWhiteSpace(window[pos]))
                pos++;

            int end = pos;
            while (end < window.Length)
            {
                char ch = window[end];
                if (char.IsDigit(ch) || ch == '-' || ch == '+' || ch == '.' || ch == 'e' || ch == 'E')
                {
                    end++;
                    continue;
                }
                break;
            }

            return end > pos &&
                   float.TryParse(
                       window.Substring(pos, end - pos),
                       NumberStyles.Float,
                       CultureInfo.InvariantCulture,
                       out value);
        }

        private void DumpTechAnchor(Dictionary<string, object> techById, string techId)
        {
            object tech;
            if (!techById.TryGetValue(techId, out tech) || tech == null)
            {
                Logger.LogInfo("AR_PROGRESSION_TECH|id=" + Esc(techId) + "|found=false");
                return;
            }

            string[] parents = Strings(Get(tech, "parents") as IList).ToArray();
            string[] craftIds = Strings(Get(tech, "crafts") as IList).ToArray();

            Logger.LogInfo(
                "AR_PROGRESSION_TECH" +
                "|id=" + Esc(techId) +
                "|found=true" +
                "|hidden=" + Bool(Get(tech, "hidden")).ToString().ToLowerInvariant() +
                "|invisible=" + Bool(Get(tech, "invisible")).ToString().ToLowerInvariant() +
                "|parents=" + Esc(string.Join(";", parents)) +
                "|crafts=" + Esc(string.Join(";", craftIds)));
        }

        private int DumpItemDisclosureChannels(
            IList items,
            Dictionary<string, object> craftById,
            Dictionary<string, object> itemById)
        {
            int rows = 0;
            foreach (object item in items)
            {
                if (item == null)
                    continue;

                IList expressions = Get(item, "on_use_expressions") as IList;
                if (expressions == null)
                    continue;

                foreach (object expression in expressions)
                {
                    string raw = ExpressionRaw(expression);
                    if (string.IsNullOrEmpty(raw))
                        continue;

                    bool random = raw.IndexOf("UnlockRandomAlchemy", StringComparison.Ordinal) >= 0;
                    bool exact = raw.IndexOf("UnlockAlchemy", StringComparison.Ordinal) >= 0;
                    if (!random && !exact)
                        continue;

                    if (random)
                    {
                        Logger.LogInfo(
                            "AR_PROGRESSION_DISCLOSURE" +
                            "|source=item_on_use" +
                            "|owner_item=" + Esc(ItemName(item)) +
                            "|mode=random" +
                            "|target=" +
                            "|arity=0" +
                            "|ordinary=false");
                        rows++;
                    }

                    if (exact)
                    {
                        string craftId = ExtractAlchemyCraftId(raw, raw.IndexOf("UnlockAlchemy", StringComparison.Ordinal));
                        rows += LogDisclosure(
                            "item_on_use",
                            ItemName(item),
                            string.Empty,
                            string.Empty,
                            craftId,
                            craftById,
                            itemById);
                    }
                }
            }

            return rows;
        }

        private int DumpUnlockOccurrences(
            string graphName,
            string serialized,
            Dictionary<string, Node> nodes,
            Dictionary<string, object> craftById,
            Dictionary<string, object> itemById,
            string marker,
            bool random)
        {
            int rows = 0;
            int start = 0;
            while (start < serialized.Length)
            {
                int pos = serialized.IndexOf(marker, start, StringComparison.Ordinal);
                if (pos < 0)
                    break;

                Node node = FindOwningNode(nodes, pos);
                string nodeType = node == null ? string.Empty : node.Type;
                string nodeId = node == null ? string.Empty : node.Id;

                if (random)
                {
                    Logger.LogInfo(
                        "AR_PROGRESSION_DISCLOSURE" +
                        "|source=flow" +
                        "|owner_item=" +
                        "|graph=" + Esc(graphName) +
                        "|node=" + Esc(nodeId) +
                        "|node_type=" + Esc(nodeType) +
                        "|mode=random" +
                        "|target=" +
                        "|arity=0" +
                        "|ordinary=false");
                    rows++;
                }
                else
                {
                    string craftId = ExtractAlchemyCraftId(serialized, pos);
                    rows += LogDisclosure(
                        "flow",
                        string.Empty,
                        graphName,
                        nodeId + "\n" + nodeType,
                        craftId,
                        craftById,
                        itemById);
                }

                start = pos + marker.Length;
            }

            return rows;
        }

        private int LogDisclosure(
            string source,
            string ownerItem,
            string graph,
            string nodeComposite,
            string craftId,
            Dictionary<string, object> craftById,
            Dictionary<string, object> itemById)
        {
            string node = string.Empty;
            string nodeType = string.Empty;
            if (!string.IsNullOrEmpty(nodeComposite))
            {
                string[] parts = nodeComposite.Split(new[] { '\n' }, 2);
                node = parts.Length > 0 ? parts[0] : string.Empty;
                nodeType = parts.Length > 1 ? parts[1] : string.Empty;
            }

            object craft;
            craftById.TryGetValue(craftId ?? string.Empty, out craft);
            string targetId = craft == null ? string.Empty : PrimaryOutput(craft);
            object targetDef;
            itemById.TryGetValue(targetId, out targetDef);
            string targetName = targetDef == null ? Localize(targetId) : ItemName(targetDef);
            int arity = craft == null ? 0 : ItemIds(Get(craft, "needs") as IList).Count();
            bool ordinary = craft != null && IsSuccessFormula(craft) && IsPickerCompatible(craft, itemById);

            Logger.LogInfo(
                "AR_PROGRESSION_DISCLOSURE" +
                "|source=" + Esc(source) +
                "|owner_item=" + Esc(ownerItem) +
                "|graph=" + Esc(graph) +
                "|node=" + Esc(node) +
                "|node_type=" + Esc(nodeType) +
                "|mode=exact" +
                "|target=" + Esc(targetName) +
                "|arity=" + arity.ToString(CultureInfo.InvariantCulture) +
                "|ordinary=" + ordinary.ToString().ToLowerInvariant() +
                "|resolved=" + (craft != null).ToString().ToLowerInvariant());

            return 1;
        }

        private static string ExtractAlchemyCraftId(string text, int markerPos)
        {
            if (string.IsNullOrEmpty(text) || markerPos < 0)
                return string.Empty;

            int pos = text.IndexOf("mix:mf_alchemy", markerPos, StringComparison.Ordinal);
            if (pos < 0 || pos - markerPos > 1400)
                return string.Empty;

            int end = pos;
            while (end < text.Length)
            {
                char ch = text[end];
                if (char.IsLetterOrDigit(ch) || ch == '_' || ch == ':' || ch == '-' || ch == '.')
                {
                    end++;
                    continue;
                }
                break;
            }

            return end > pos ? text.Substring(pos, end - pos) : string.Empty;
        }

        private static Node FindOwningNode(Dictionary<string, Node> nodes, int contentPosition)
        {
            Node best = null;
            int bestDelta = int.MaxValue;
            foreach (Node node in nodes.Values)
            {
                if (node.TypePosition < contentPosition)
                    continue;

                int delta = node.TypePosition - contentPosition;
                if (delta <= 6000 && delta < bestDelta)
                {
                    best = node;
                    bestDelta = delta;
                }
            }
            return best;
        }

        private void DumpFocusGraph(
            string graphName,
            string serialized,
            Dictionary<string, Node> nodes,
            List<Connection> connections)
        {
            var seedIds = new HashSet<string>(StringComparer.Ordinal);
            foreach (Node node in nodes.Values)
            {
                string window = NodeWindow(serialized, node, 5000);
                for (int i = 0; i < FocusTerms.Length; i++)
                {
                    if (window.IndexOf(FocusTerms[i], StringComparison.OrdinalIgnoreCase) >= 0)
                    {
                        seedIds.Add(node.Id);
                        break;
                    }
                }
            }

            if (seedIds.Count == 0)
                return;

            var neighbors = new Dictionary<string, HashSet<string>>(StringComparer.Ordinal);
            Action<string, string> addNeighbor = delegate(string a, string b)
            {
                HashSet<string> set;
                if (!neighbors.TryGetValue(a, out set))
                    neighbors[a] = set = new HashSet<string>(StringComparer.Ordinal);
                set.Add(b);
            };

            foreach (Connection c in connections)
            {
                addNeighbor(c.SourceNode, c.TargetNode);
                addNeighbor(c.TargetNode, c.SourceNode);
            }

            var byUid = new Dictionary<string, List<string>>(StringComparer.Ordinal);
            foreach (Node node in nodes.Values)
            {
                if (!string.IsNullOrEmpty(node.Uid))
                {
                    List<string> ids;
                    if (!byUid.TryGetValue(node.Uid, out ids))
                        byUid[node.Uid] = ids = new List<string>();
                    ids.Add(node.Id);
                }
            }

            foreach (Node node in nodes.Values)
            {
                if (string.IsNullOrEmpty(node.SourceOutputUid))
                    continue;

                List<string> targets;
                if (!byUid.TryGetValue(node.SourceOutputUid, out targets))
                    continue;

                foreach (string target in targets)
                {
                    addNeighbor(node.Id, target);
                    addNeighbor(target, node.Id);
                }
            }

            var retained = new HashSet<string>(seedIds, StringComparer.Ordinal);
            var frontier = new HashSet<string>(seedIds, StringComparer.Ordinal);
            for (int depth = 0; depth < 4; depth++)
            {
                var next = new HashSet<string>(StringComparer.Ordinal);
                foreach (string id in frontier)
                {
                    HashSet<string> set;
                    if (!neighbors.TryGetValue(id, out set))
                        continue;

                    foreach (string other in set)
                        if (retained.Add(other))
                            next.Add(other);
                }

                frontier = next;
                if (frontier.Count == 0)
                    break;
            }

            List<Node> ordered = retained
                .Where(nodes.ContainsKey)
                .Select(delegate(string id) { return nodes[id]; })
                .OrderBy(delegate(Node n) { return n.TypePosition; })
                .Take(160)
                .ToList();

            var finalIds = new HashSet<string>(
                ordered.Select(delegate(Node n) { return n.Id; }),
                StringComparer.Ordinal);

            Logger.LogInfo(
                "AR_PROGRESSION_FOCUS_BEGIN" +
                "|graph=" + Esc(graphName) +
                "|seeds=" + seedIds.Count.ToString(CultureInfo.InvariantCulture) +
                "|nodes=" + ordered.Count.ToString(CultureInfo.InvariantCulture));

            foreach (Node node in ordered)
            {
                string window = NodeWindow(serialized, node, 5000);
                string[] hits = FocusTerms
                    .Where(delegate(string term)
                    {
                        return window.IndexOf(term, StringComparison.OrdinalIgnoreCase) >= 0;
                    })
                    .Distinct(StringComparer.OrdinalIgnoreCase)
                    .ToArray();

                string task = ReadNodeContent(serialized, node, "Task");
                string npc = ReadNodeContent(serialized, node, "NPC id");
                string state = ReadNodeContent(serialized, node, "State");
                string phrase = ReadNodeContent(serialized, node, "Phrase") ??
                                ReadNodeContent(serialized, node, "phrase");
                string identifier = ReadNodeIdentifier(serialized, node);
                string answers = node.Type.EndsWith("Flow_MultiAnswer", StringComparison.Ordinal)
                    ? string.Join(";", ReadMultiAnswers(serialized, node))
                    : string.Empty;

                Logger.LogInfo(
                    "AR_PROGRESSION_FOCUS_NODE" +
                    "|graph=" + Esc(graphName) +
                    "|node=" + Esc(node.Id) +
                    "|type=" + Esc(node.Type) +
                    "|task=" + Esc(Sanitize(task)) +
                    "|npc=" + Esc(Sanitize(npc)) +
                    "|state=" + Esc(Sanitize(state)) +
                    "|phrase=" + Esc(Sanitize(phrase)) +
                    "|identifier=" + Esc(Sanitize(identifier)) +
                    "|answers=" + Esc(Sanitize(answers)) +
                    "|focus=" + Esc(string.Join(";", hits)));
            }

            foreach (Connection c in connections)
            {
                if (!finalIds.Contains(c.SourceNode) || !finalIds.Contains(c.TargetNode))
                    continue;

                Logger.LogInfo(
                    "AR_PROGRESSION_FOCUS_EDGE" +
                    "|graph=" + Esc(graphName) +
                    "|from=" + Esc(c.SourceNode) +
                    "|to=" + Esc(c.TargetNode) +
                    "|source_port=" + Esc(c.SourcePort) +
                    "|target_port=" + Esc(c.TargetPort) +
                    "|kind=serialized");
            }

            foreach (Node node in ordered)
            {
                if (string.IsNullOrEmpty(node.SourceOutputUid))
                    continue;

                List<string> targets;
                if (!byUid.TryGetValue(node.SourceOutputUid, out targets))
                    continue;

                foreach (string target in targets)
                {
                    if (!finalIds.Contains(target))
                        continue;

                    Logger.LogInfo(
                        "AR_PROGRESSION_FOCUS_EDGE" +
                        "|graph=" + Esc(graphName) +
                        "|from=" + Esc(node.Id) +
                        "|to=" + Esc(target) +
                        "|source_port=" +
                        "|target_port=" +
                        "|kind=custom_function");
                }
            }

            Logger.LogInfo("AR_PROGRESSION_FOCUS_DONE|graph=" + Esc(graphName));
        }

        private static bool IsFocusGraph(string graphName, string serialized)
        {
            if (!string.IsNullOrEmpty(graphName) &&
                (graphName.IndexOf("npc_witch", StringComparison.OrdinalIgnoreCase) >= 0 ||
                 graphName.IndexOf("npc_merchant", StringComparison.OrdinalIgnoreCase) >= 0))
                return true;

            for (int i = 0; i < FocusTerms.Length; i++)
                if (serialized.IndexOf(FocusTerms[i], StringComparison.OrdinalIgnoreCase) >= 0)
                    return true;

            return false;
        }

        private static string GraphName(UnityEngine.Object controller, object graph)
        {
            Component component = controller as Component;
            string goName = component != null && component.gameObject != null
                ? component.gameObject.name
                : string.Empty;
            string graphName = Str(Get(graph, "name"));
            if (string.IsNullOrEmpty(graphName))
                graphName = Str(Get(graph, "_name"));

            if (string.IsNullOrEmpty(goName))
                return graphName;
            if (string.IsNullOrEmpty(graphName) || string.Equals(goName, graphName, StringComparison.Ordinal))
                return goName;
            return goName + "/" + graphName;
        }

        private static Dictionary<string, Node> BuildNodeIndex(string serialized)
        {
            var result = new Dictionary<string, Node>(StringComparer.Ordinal);
            const string typeMarker = "\"$type\":\"";
            const string idMarker = "\"$id\":\"";
            int start = 0;
            while (start < serialized.Length)
            {
                int typePos = serialized.IndexOf(typeMarker, start, StringComparison.Ordinal);
                if (typePos < 0) break;
                int typeEnd;
                string type = ReadJsonString(serialized, typePos + typeMarker.Length, out typeEnd);
                if (type == null) break;
                int nextType = serialized.IndexOf(typeMarker, typeEnd, StringComparison.Ordinal);
                int idPos = serialized.IndexOf(idMarker, typeEnd, StringComparison.Ordinal);
                if (idPos >= 0 && (nextType < 0 || idPos < nextType) && idPos - typeEnd < 240)
                {
                    int idEnd;
                    string id = ReadJsonString(serialized, idPos + idMarker.Length, out idEnd);
                    if (!string.IsNullOrEmpty(id))
                    {
                        var node = new Node { Id = id, Type = type, TypePosition = typePos };
                        node.Uid = ReadRawStringProperty(serialized, node, "_UID");
                        node.SourceOutputUid = ReadRawStringProperty(serialized, node, "_sourceOutputUID");
                        result[id] = node;
                    }
                }
                start = typeEnd + 1;
            }
            return result;
        }

        private static List<Connection> ParseConnections(string serialized)
        {
            var result = new List<Connection>();
            const string spMarker = "\"_sourcePortName\":\"";
            const string tpMarker = "\"_targetPortName\":\"";
            const string srcMarker = "\"_sourceNode\":{\"$ref\":\"";
            const string dstMarker = "\"_targetNode\":{\"$ref\":\"";
            int start = 0;
            while (start < serialized.Length)
            {
                int spPos = serialized.IndexOf(spMarker, start, StringComparison.Ordinal);
                if (spPos < 0) break;
                int spEnd;
                string sp = ReadJsonString(serialized, spPos + spMarker.Length, out spEnd);
                int tpPos = serialized.IndexOf(tpMarker, spEnd, StringComparison.Ordinal);
                if (tpPos < 0 || tpPos - spEnd > 300) { start = spEnd + 1; continue; }
                int tpEnd;
                string tp = ReadJsonString(serialized, tpPos + tpMarker.Length, out tpEnd);
                int srcPos = serialized.IndexOf(srcMarker, tpEnd, StringComparison.Ordinal);
                if (srcPos < 0 || srcPos - tpEnd > 300) { start = tpEnd + 1; continue; }
                int srcEnd;
                string src = ReadJsonString(serialized, srcPos + srcMarker.Length, out srcEnd);
                int dstPos = serialized.IndexOf(dstMarker, srcEnd, StringComparison.Ordinal);
                if (dstPos < 0 || dstPos - srcEnd > 300) { start = srcEnd + 1; continue; }
                int dstEnd;
                string dst = ReadJsonString(serialized, dstPos + dstMarker.Length, out dstEnd);
                if (!string.IsNullOrEmpty(src) && !string.IsNullOrEmpty(dst))
                    result.Add(new Connection { SourcePort = sp, TargetPort = tp, SourceNode = src, TargetNode = dst });
                start = dstEnd + 1;
            }
            return result;
        }

        private static string NodeWindow(string serialized, Node node, int lookBehind)
        {
            if (node == null) return string.Empty;
            int begin = Math.Max(0, node.TypePosition - lookBehind);
            return serialized.Substring(begin, node.TypePosition - begin);
        }

        private static string ReadNodeContent(string serialized, Node node, string key)
        {
            if (node == null) return null;
            string window = NodeWindow(serialized, node, 3000);
            string marker = "\"" + key + "\":{\"$content\":\"";
            int pos = window.LastIndexOf(marker, StringComparison.Ordinal);
            if (pos < 0) return null;
            int end;
            return ReadJsonString(window, pos + marker.Length, out end);
        }

        private static string ReadNodeIdentifier(string serialized, Node node)
        {
            if (node == null) return null;
            string window = NodeWindow(serialized, node, 3000);
            const string marker = "\"identifier\":\"";
            int pos = window.LastIndexOf(marker, StringComparison.Ordinal);
            if (pos < 0) return null;
            int end;
            return ReadJsonString(window, pos + marker.Length, out end);
        }

        private static string ReadRawStringProperty(string serialized, Node node, string key)
        {
            if (node == null) return null;
            string window = NodeWindow(serialized, node, 3000);
            string marker = "\"" + key + "\":\"";
            int pos = window.LastIndexOf(marker, StringComparison.Ordinal);
            if (pos < 0) return null;
            int end;
            return ReadJsonString(window, pos + marker.Length, out end);
        }

        private static List<string> ReadMultiAnswers(string serialized, Node node)
        {
            var result = new List<string>();
            if (node == null) return result;
            string window = NodeWindow(serialized, node, 18000);
            const string marker = "\"answers\":[";
            int pos = window.LastIndexOf(marker, StringComparison.Ordinal);
            if (pos < 0) return result;
            int i = pos + marker.Length;
            while (i < window.Length)
            {
                while (i < window.Length && (char.IsWhiteSpace(window[i]) || window[i] == ',')) i++;
                if (i >= window.Length || window[i] == ']') break;
                if (window[i] != '"') break;
                int end;
                string value = ReadJsonString(window, i + 1, out end);
                if (value == null) break;
                result.Add(value);
                i = end + 1;
            }
            return result;
        }

        private static string ReadJsonString(string text, int start, out int end)
        {
            end = start;
            bool escaped = false;
            for (int i = start; i < text.Length; i++)
            {
                char ch = text[i];
                if (escaped) { escaped = false; continue; }
                if (ch == '\\') { escaped = true; continue; }
                if (ch != '"') continue;
                end = i;
                string raw = text.Substring(start, i - start);
                try { return Regex.Unescape(raw.Replace("\\/", "/")); }
                catch { return raw; }
            }
            return null;
        }

        private static string Sanitize(string value)
        {
            if (string.IsNullOrEmpty(value)) return value ?? string.Empty;
            return Regex.Replace(value, @"mix:mf_alchemy[A-Za-z0-9_:\-\.]*", "<alchemy_formula>", RegexOptions.CultureInvariant);
        }

        private static Dictionary<string, object> IndexById(IList list)
        {
            var result = new Dictionary<string, object>(StringComparer.Ordinal);
            foreach (object obj in list)
            {
                if (obj == null) continue;
                string id = Id(obj);
                if (id.Length > 0 && !result.ContainsKey(id)) result[id] = obj;
            }
            return result;
        }

        private static IEnumerable<string> Strings(IList list)
        {
            if (list == null) yield break;
            foreach (object value in list)
            {
                string text = Str(value);
                if (text.Length > 0) yield return text;
            }
        }

        private static IEnumerable<string> ItemIds(IList list)
        {
            if (list == null) yield break;
            foreach (object item in list)
            {
                string id = Id(item);
                if (id.Length > 0) yield return id;
            }
        }

        private string ItemName(object def)
        {
            if (def == null) return string.Empty;
            object name = Invoke(def, "GetItemName", true);
            string value = Str(name);
            return string.IsNullOrEmpty(value) ? Localize(Id(def)) : value;
        }

        private static string ExpressionRaw(object expression)
        {
            if (expression == null) return string.Empty;
            return Str(Invoke(expression, "GetRawExpressionString"));
        }

        private static bool IsSuccessFormula(object craft)
        {
            string id = Id(craft);
            return id.StartsWith("mix:", StringComparison.Ordinal)
                   && id.IndexOf("goo", StringComparison.Ordinal) < 0
                   && id.IndexOf(":_:", StringComparison.Ordinal) < 0;
        }

        private static bool IsPickerCompatible(object craft, Dictionary<string, object> itemById)
        {
            string[] needs = ItemIds(Get(craft, "needs") as IList).ToArray();
            if (needs.Length != 2 && needs.Length != 3) return false;

            string[] expected = { "Powder", "Fluid", "Essence" };
            var seen = new HashSet<string>(StringComparer.Ordinal);
            for (int i = 0; i < needs.Length; i++)
            {
                if (!seen.Add(needs[i])) return false;
                object def;
                if (!itemById.TryGetValue(needs[i], out def) || def == null) return false;
                string type = Str(Get(def, "alch_type"));
                if (type != expected[i] && type != "Universal") return false;
            }
            return true;
        }

        private static string PrimaryOutput(object craft)
        {
            IList output = Get(craft, "output") as IList;
            if (output == null) return string.Empty;
            foreach (object item in output)
            {
                string id = Id(item);
                if (id == "r" || id == "g" || id == "b" || id == "v" || id == "gratitude_points") continue;
                if (id.Length > 0) return id;
            }
            return string.Empty;
        }

        private bool BindGame()
        {
            if (_gameAssembly != null) return true;
            _gameAssembly = AppDomain.CurrentDomain.GetAssemblies()
                .FirstOrDefault(delegate(Assembly a) { return a.GetName().Name == "Assembly-CSharp"; });
            return _gameAssembly != null;
        }

        private static Type FindType(string name)
        {
            foreach (Assembly assembly in AppDomain.CurrentDomain.GetAssemblies())
            {
                Type direct = assembly.GetType(name, false);
                if (direct != null) return direct;
                try
                {
                    Type byName = assembly.GetTypes().FirstOrDefault(delegate(Type t) { return t != null && t.Name == name; });
                    if (byName != null) return byName;
                }
                catch (ReflectionTypeLoadException ex)
                {
                    Type byName = ex.Types.FirstOrDefault(delegate(Type t) { return t != null && t.Name == name; });
                    if (byName != null) return byName;
                }
            }
            return null;
        }

        private void InitLocalization()
        {
            _gjlType = FindType("GJL");
            if (_gjlType == null) return;
            _localize = _gjlType.GetMethods(Stat)
                .FirstOrDefault(delegate(MethodInfo m)
                {
                    ParameterInfo[] p = m.GetParameters();
                    return m.Name == "L" && m.ReturnType == typeof(string) &&
                           p.Length == 1 && p[0].ParameterType == typeof(string);
                });
        }

        private string Localize(string key)
        {
            if (string.IsNullOrEmpty(key) || _gjlType == null || _localize == null) return key ?? string.Empty;
            try { return Str(_localize.Invoke(null, new object[] { key })); }
            catch { return key; }
        }

        private static object Invoke(object obj, string name, params object[] args)
        {
            if (obj == null) return null;
            for (Type type = obj.GetType(); type != null; type = type.BaseType)
            {
                foreach (MethodInfo method in type.GetMethods(Inst))
                {
                    if (method.Name != name || method.GetParameters().Length != args.Length) continue;
                    try { return method.Invoke(obj, args); }
                    catch (TargetInvocationException) { throw; }
                    catch { }
                }
            }
            return null;
        }

        private static object Get(object obj, string name)
        {
            if (obj == null) return null;
            for (Type type = obj.GetType(); type != null; type = type.BaseType)
            {
                FieldInfo field = type.GetField(name, Inst);
                if (field != null) return field.GetValue(obj);
                PropertyInfo property = type.GetProperty(name, Inst);
                if (property != null && property.CanRead) return property.GetValue(obj, null);
            }
            return null;
        }

        private static object GetStatic(Type type, string name)
        {
            if (type == null) return null;
            for (Type current = type; current != null; current = current.BaseType)
            {
                FieldInfo field = current.GetField(name, Stat);
                if (field != null) return field.GetValue(null);
                PropertyInfo property = current.GetProperty(name, Stat);
                if (property != null && property.CanRead) return property.GetValue(null, null);
            }
            return null;
        }

        private static string Id(object obj) { return Get(obj, "id") as string ?? string.Empty; }
        private static string Str(object obj) { return Convert.ToString(obj, CultureInfo.InvariantCulture) ?? string.Empty; }

        private static bool Bool(object obj)
        {
            try { return obj != null && Convert.ToBoolean(obj, CultureInfo.InvariantCulture); }
            catch { return false; }
        }

        private static string Esc(string value)
        {
            if (string.IsNullOrEmpty(value)) return string.Empty;
            return value.Replace("\\", "\\\\").Replace("|", "\\|").Replace("\r", " ").Replace("\n", " ");
        }
    }
}
