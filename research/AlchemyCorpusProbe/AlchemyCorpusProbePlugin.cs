// SPDX-License-Identifier: MPL-2.0
using BepInEx;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Reflection;

namespace NikichMods.AlchemyRiddle.Research
{
    [BepInPlugin(Guid, Name, Version)]
    public sealed class AlchemyCorpusProbePlugin : BaseUnityPlugin
    {
        public const string Guid = "nikich.graveyardkeeper.alchemyriddle.corpusprobe";
        public const string Name = "AlchemyRiddle Corpus Probe";
        public const string Version = "0.2.0";

        private static readonly BindingFlags Inst =
            BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic;
        private static readonly BindingFlags Stat =
            BindingFlags.Static | BindingFlags.Public | BindingFlags.NonPublic;

        private static readonly HashSet<string> TechOutputs =
            new HashSet<string>(
                new[] { "r", "g", "b", "v", "gratitude_points" },
                StringComparer.Ordinal);

        private Assembly _gameAssembly;
        private bool _dumped;

        private void Awake()
        {
            Logger.LogInfo("AlchemyRiddle Corpus Probe 0.2.0 loaded. Read-only research probe.");
            StartCoroutine(DumpWhenReady());
        }

        private IEnumerator DumpWhenReady()
        {
            while (!_dumped)
            {
                if (BindGame())
                {
                    Type mainGame = GameType("MainGame");
                    Type balanceType = GameType("GameBalance");

                    if (Bool(GetStatic(mainGame, "game_started")))
                    {
                        object balance = GetStatic(balanceType, "me");
                        if (balance != null)
                        {
                            try
                            {
                                Dump(balance);
                            }
                            catch (Exception ex)
                            {
                                Logger.LogError("AR_CORPUS_ERROR|" + Esc(ex.ToString()));
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

            if (items == null || crafts == null)
                throw new InvalidOperationException("GameBalance items_data/craft_data not available.");

            List<object> alchemyCrafts = new List<object>();

            foreach (object craft in crafts)
            {
                if (craft == null)
                    continue;

                if (!string.Equals(Str(Get(craft, "craft_type")), "MixedCraft", StringComparison.Ordinal))
                    continue;

                string id = Id(craft);
                if (!id.StartsWith("mix:mf_alchemy", StringComparison.Ordinal))
                    continue;

                alchemyCrafts.Add(craft);
            }

            List<object> successCrafts = alchemyCrafts.Where(IsSuccessFormula).ToList();
            List<object> auxCrafts = alchemyCrafts.Where(delegate(object x) { return !IsSuccessFormula(x); }).ToList();

            List<string> stations = alchemyCrafts
                .Select(StationId)
                .Where(delegate(string x) { return x.Length > 0; })
                .Distinct(StringComparer.Ordinal)
                .OrderBy(delegate(string x) { return x; }, StringComparer.Ordinal)
                .ToList();

            Dictionary<string, string> stationSymbols = Symbols(stations, "W");

            SortedSet<string> needIds = new SortedSet<string>(StringComparer.Ordinal);
            foreach (object craft in alchemyCrafts)
            {
                foreach (string id in ItemIds(Get(craft, "needs") as IList))
                    needIds.Add(id);
            }

            Type itemDefinitionType = GameType("ItemDefinition");
            MethodInfo gooMethod = itemDefinitionType == null
                ? null
                : itemDefinitionType.GetMethod(
                    "GetGooFromAlchemyIngridient",
                    BindingFlags.Static | BindingFlags.Public | BindingFlags.NonPublic,
                    null,
                    new[] { typeof(string) },
                    null);

            List<Tuple<string, string>> gooPairs = new List<Tuple<string, string>>();
            string[] needSnapshot = needIds.ToArray();

            foreach (string raw in needSnapshot)
            {
                string goo = gooMethod == null
                    ? string.Empty
                    : Str(gooMethod.Invoke(null, new object[] { raw }));

                if (goo.Length == 0)
                    continue;

                needIds.Add(goo);
                gooPairs.Add(Tuple.Create(raw, goo));
            }

            Dictionary<string, string> needSymbols = Symbols(needIds.ToList(), "N");

            SortedSet<string> outputIds = new SortedSet<string>(StringComparer.Ordinal);
            foreach (object craft in alchemyCrafts)
            {
                string output = PrimaryOutput(craft);
                if (output.Length > 0)
                    outputIds.Add(output);
            }

            Dictionary<string, string> outputSymbols = Symbols(outputIds.ToList(), "O");

            Dictionary<string, object> itemById = new Dictionary<string, object>(StringComparer.Ordinal);
            foreach (object def in items)
            {
                if (def == null)
                    continue;

                string id = Id(def);
                if (id.Length > 0 && !itemById.ContainsKey(id))
                    itemById[id] = def;
            }

            Logger.LogInfo(
                "AR_CORPUS_BEGIN|probe=0.2.0|target=GraveyardKeeper-1.407|source=loaded-GameBalance");
            Logger.LogInfo(
                "AR_CORPUS_SOURCE|decompile_reference=Kupie/GYK_DECOMP@6abf79199d92482af1c7573870dd9a20ec2270b9");
            Logger.LogInfo(
                "AR_CORPUS_SUMMARY" +
                "|alchemy_mixed_defs=" + alchemyCrafts.Count.ToString(CultureInfo.InvariantCulture) +
                "|success_formulas=" + successCrafts.Count.ToString(CultureInfo.InvariantCulture) +
                "|aux_failure_defs=" + auxCrafts.Count.ToString(CultureInfo.InvariantCulture) +
                "|stations=" + stations.Count.ToString(CultureInfo.InvariantCulture) +
                "|need_symbols=" + needSymbols.Count.ToString(CultureInfo.InvariantCulture) +
                "|output_symbols=" + outputSymbols.Count.ToString(CultureInfo.InvariantCulture));

            foreach (string station in stations)
            {
                List<object> scoped = alchemyCrafts
                    .Where(delegate(object c) { return StationId(c) == station; })
                    .ToList();

                List<object> scopedSuccess = scoped.Where(IsSuccessFormula).ToList();

                List<int> outputMultiplicity = scopedSuccess
                    .GroupBy(PrimaryOutput, StringComparer.Ordinal)
                    .Where(delegate(IGrouping<string, object> g) { return g.Key.Length > 0; })
                    .Select(delegate(IGrouping<string, object> g) { return g.Count(); })
                    .ToList();

                string[] arities = scopedSuccess
                    .GroupBy(delegate(object c) { return Count(Get(c, "needs") as IList); })
                    .OrderBy(delegate(IGrouping<int, object> g) { return g.Key; })
                    .Select(delegate(IGrouping<int, object> g)
                    {
                        return g.Key.ToString(CultureInfo.InvariantCulture) + ":" +
                               g.Count().ToString(CultureInfo.InvariantCulture);
                    })
                    .ToArray();

                Logger.LogInfo(
                    "AR_STATION" +
                    "|station=" + stationSymbols[station] +
                    "|defs=" + scoped.Count.ToString(CultureInfo.InvariantCulture) +
                    "|success=" + scopedSuccess.Count.ToString(CultureInfo.InvariantCulture) +
                    "|aux=" + (scoped.Count - scopedSuccess.Count).ToString(CultureInfo.InvariantCulture) +
                    "|arities=" + string.Join(",", arities) +
                    "|distinct_outputs=" + outputMultiplicity.Count.ToString(CultureInfo.InvariantCulture) +
                    "|multi_formula_outputs=" + outputMultiplicity.Count(delegate(int x) { return x > 1; }).ToString(CultureInfo.InvariantCulture) +
                    "|max_formulas_per_output=" +
                    (outputMultiplicity.Count == 0 ? 0 : outputMultiplicity.Max()).ToString(CultureInfo.InvariantCulture));
            }

            HashSet<string> successNeedIds =
                new HashSet<string>(
                    successCrafts.SelectMany(delegate(object c)
                    {
                        return ItemIds(Get(c, "needs") as IList);
                    }),
                    StringComparer.Ordinal);

            foreach (KeyValuePair<string, string> pair in
                needSymbols.OrderBy(delegate(KeyValuePair<string, string> x) { return x.Value; }, StringComparer.Ordinal))
            {
                object def;
                itemById.TryGetValue(pair.Key, out def);

                Logger.LogInfo(
                    "AR_ITEM" +
                    "|item=" + pair.Value +
                    "|alchemy_type=" + Esc(Str(Get(def, "alch_type"))) +
                    "|used_in_success=" + (successNeedIds.Contains(pair.Key) ? "true" : "false"));
            }

            foreach (Tuple<string, string> pair in gooPairs
                .Where(delegate(Tuple<string, string> p)
                {
                    return needSymbols.ContainsKey(p.Item1) && needSymbols.ContainsKey(p.Item2);
                })
                .OrderBy(delegate(Tuple<string, string> p) { return needSymbols[p.Item1]; }, StringComparer.Ordinal))
            {
                Logger.LogInfo(
                    "AR_GOO_MAP|from=" + needSymbols[pair.Item1] +
                    "|to=" + needSymbols[pair.Item2]);
            }

            int successIndex = 0;
            int auxIndex = 0;

            foreach (object craft in alchemyCrafts
                .OrderBy(StationId, StringComparer.Ordinal)
                .ThenBy(Id, StringComparer.Ordinal))
            {
                bool success = IsSuccessFormula(craft);
                int index = success ? ++successIndex : ++auxIndex;

                string[] needs = ItemIds(Get(craft, "needs") as IList)
                    .Select(delegate(string x)
                    {
                        return needSymbols.ContainsKey(x) ? needSymbols[x] : "?";
                    })
                    .ToArray();

                string rawOutput = PrimaryOutput(craft);
                string output = outputSymbols.ContainsKey(rawOutput)
                    ? outputSymbols[rawOutput]
                    : string.Empty;

                string station = StationId(craft);
                string stationSymbol = stationSymbols.ContainsKey(station)
                    ? stationSymbols[station]
                    : "?";

                Logger.LogInfo(
                    "AR_RECIPE" +
                    "|kind=" + (success ? "success" : "aux") +
                    "|recipe=" + (success ? "S" : "A") + index.ToString("D4", CultureInfo.InvariantCulture) +
                    "|station=" + stationSymbol +
                    "|arity=" + needs.Length.ToString(CultureInfo.InvariantCulture) +
                    "|needs=" + string.Join(",", needs) +
                    "|output=" + output +
                    "|needs_unlock=" + Bool(Get(craft, "needs_unlock")).ToString().ToLowerInvariant() +
                    "|hidden=" + Bool(Get(craft, "hidden")).ToString().ToLowerInvariant());
            }

            Dictionary<string, int> eligibleCounts =
                new Dictionary<string, int>(StringComparer.Ordinal);

            foreach (object def in items)
            {
                if (def == null)
                    continue;

                string type = Str(Get(def, "alch_type"));
                if (type != "Powder" && type != "Fluid" && type != "Essence" && type != "Universal")
                    continue;

                int count;
                eligibleCounts.TryGetValue(type, out count);
                eligibleCounts[type] = count + 1;
            }

            foreach (string type in new[] { "Powder", "Fluid", "Essence", "Universal" })
            {
                int count;
                eligibleCounts.TryGetValue(type, out count);

                Logger.LogInfo(
                    "AR_ELIGIBLE|alchemy_type=" + type +
                    "|item_definitions=" + count.ToString(CultureInfo.InvariantCulture));
            }

            DumpExposure(balance, items, crafts, successCrafts, itemById);

            Logger.LogInfo(
                "AR_CORPUS_DONE|probe=0.2.0" +
                "|success_records=" + successIndex.ToString(CultureInfo.InvariantCulture) +
                "|aux_records=" + auxIndex.ToString(CultureInfo.InvariantCulture));
        }

        private void DumpExposure(
            object balance,
            IList items,
            IList crafts,
            List<object> successCrafts,
            Dictionary<string, object> itemById)
        {
            IList objectCrafts = Get(balance, "craft_obj_data") as IList;
            IList techs = Get(balance, "techs_data") as IList;
            IList vendors = Get(balance, "vendors_data") as IList;
            IList quests = Get(balance, "quests_data") as IList;

            if (objectCrafts == null || techs == null || vendors == null || quests == null)
                throw new InvalidOperationException("Exposure probe requires craft_obj_data, techs_data, vendors_data and quests_data.");

            List<object> ordinarySuccess = successCrafts
                .Where(delegate(object c) { return IsPickerCompatible(c, itemById); })
                .ToList();

            List<string> targets = ordinarySuccess
                .Select(PrimaryOutput)
                .Where(delegate(string x) { return x.Length > 0; })
                .Distinct(StringComparer.Ordinal)
                .OrderBy(delegate(string x) { return x; }, StringComparer.Ordinal)
                .ToList();

            Dictionary<string, string> targetSymbols = Symbols(targets, "T");
            Dictionary<string, object> craftById = IndexById(crafts);
            Dictionary<string, object> objectCraftById = IndexById(objectCrafts);

            int techTargets = 0;
            int defaultTargets = 0;
            int structuralTargets = 0;
            int vendorTargets = 0;
            int questTargets = 0;
            int anyTargets = 0;
            int uncoveredTargets = 0;

            Logger.LogInfo(
                "AR_EXPOSURE_BEGIN|probe=0.2.0" +
                "|ordinary_formulas=" + ordinarySuccess.Count.ToString(CultureInfo.InvariantCulture) +
                "|ordinary_outputs=" + targets.Count.ToString(CultureInfo.InvariantCulture) +
                "|scope=authored-demand-plus-static-sample-candidates");

            foreach (string target in targets)
            {
                object itemDef;
                itemById.TryGetValue(target, out itemDef);

                HashSet<string> ordinaryConsumers = new HashSet<string>(StringComparer.Ordinal);
                HashSet<string> blueprintConsumers = new HashSet<string>(StringComparer.Ordinal);
                HashSet<string> defaultVisibleConsumers = new HashSet<string>(StringComparer.Ordinal);
                HashSet<string> techVisibleConsumers = new HashSet<string>(StringComparer.Ordinal);
                HashSet<string> techPublicNodes = new HashSet<string>(StringComparer.Ordinal);
                HashSet<string> techGatedNodes = new HashSet<string>(StringComparer.Ordinal);
                HashSet<string> hiddenTechUnlockConsumers = new HashSet<string>(StringComparer.Ordinal);

                foreach (object craft in crafts)
                {
                    if (craft == null || !IsDownstreamConsumerCraft(craft) || !NeedsItem(craft, target))
                        continue;

                    string id = Id(craft);
                    if (id.Length == 0)
                        continue;

                    ordinaryConsumers.Add(id);
                    if (!Bool(Get(craft, "hidden")) && !Bool(Get(craft, "needs_unlock")))
                        defaultVisibleConsumers.Add(id);
                }

                foreach (object craft in objectCrafts)
                {
                    if (craft == null || !NeedsItem(craft, target))
                        continue;

                    string id = Id(craft);
                    if (id.Length == 0)
                        continue;

                    blueprintConsumers.Add(id);
                    if (!Bool(Get(craft, "hidden")) && !Bool(Get(craft, "needs_unlock")))
                        defaultVisibleConsumers.Add(id);
                }

                foreach (object tech in techs)
                {
                    if (tech == null)
                        continue;

                    string techId = Id(tech);
                    IList refs = Get(tech, "crafts") as IList;
                    if (refs == null)
                        continue;

                    foreach (object rawObj in refs)
                    {
                        string raw = Convert.ToString(rawObj, CultureInfo.InvariantCulture) ?? string.Empty;
                        if (raw.Length == 0)
                            continue;

                        bool visibleUnlock = raw[0] != '@';
                        string refId = visibleUnlock ? raw : raw.Substring(1);

                        object consumer;
                        if (!craftById.TryGetValue(refId, out consumer))
                            objectCraftById.TryGetValue(refId, out consumer);

                        if (consumer == null || Bool(Get(consumer, "hidden")) || !NeedsItem(consumer, target))
                            continue;

                        if (!visibleUnlock)
                        {
                            hiddenTechUnlockConsumers.Add(refId);
                            continue;
                        }

                        techVisibleConsumers.Add(refId);
                        if (techId.Length > 0)
                        {
                            if (Bool(Get(tech, "hidden")) || Bool(Get(tech, "invisible")))
                                techGatedNodes.Add(techId);
                            else
                                techPublicNodes.Add(techId);
                        }
                    }
                }

                int vendorCandidates = 0;
                if (itemDef != null)
                {
                    foreach (object vendor in vendors)
                    {
                        if (vendor != null && StaticVendorCanStock(vendor, itemDef, target))
                            vendorCandidates++;
                    }
                }

                int questRefs = 0;
                foreach (object quest in quests)
                {
                    if (quest != null && Bool(Get(quest, "quest_visible")) && QuestReferencesItem(quest, target))
                        questRefs++;
                }

                int formulas = ordinarySuccess.Count(delegate(object c)
                {
                    return string.Equals(PrimaryOutput(c), target, StringComparison.Ordinal);
                });

                bool hasTech = techVisibleConsumers.Count > 0;
                bool hasDefault = defaultVisibleConsumers.Count > 0;
                bool hasStructural = hasTech || hasDefault;
                bool hasVendor = vendorCandidates > 0;
                bool hasQuest = questRefs > 0;
                bool hasAny = hasStructural || hasVendor || hasQuest;

                if (hasTech) techTargets++;
                if (hasDefault) defaultTargets++;
                if (hasStructural) structuralTargets++;
                if (hasVendor) vendorTargets++;
                if (hasQuest) questTargets++;
                if (hasAny) anyTargets++; else uncoveredTargets++;

                Logger.LogInfo(
                    "AR_EXPOSURE" +
                    "|target=" + targetSymbols[target] +
                    "|formulas=" + formulas.ToString(CultureInfo.InvariantCulture) +
                    "|ordinary_consumers=" + ordinaryConsumers.Count.ToString(CultureInfo.InvariantCulture) +
                    "|blueprint_consumers=" + blueprintConsumers.Count.ToString(CultureInfo.InvariantCulture) +
                    "|default_visible_consumers=" + defaultVisibleConsumers.Count.ToString(CultureInfo.InvariantCulture) +
                    "|tech_visible_consumers=" + techVisibleConsumers.Count.ToString(CultureInfo.InvariantCulture) +
                    "|tech_public_nodes=" + techPublicNodes.Count.ToString(CultureInfo.InvariantCulture) +
                    "|tech_gated_nodes=" + techGatedNodes.Count.ToString(CultureInfo.InvariantCulture) +
                    "|tech_hidden_unlock_consumers=" + hiddenTechUnlockConsumers.Count.ToString(CultureInfo.InvariantCulture) +
                    "|vendor_static_stock_candidates=" + vendorCandidates.ToString(CultureInfo.InvariantCulture) +
                    "|visible_quest_expression_refs=" + questRefs.ToString(CultureInfo.InvariantCulture) +
                    "|structural_entry=" + hasStructural.ToString().ToLowerInvariant() +
                    "|any_candidate_entry=" + hasAny.ToString().ToLowerInvariant());
            }

            Logger.LogInfo(
                "AR_EXPOSURE_SUMMARY" +
                "|targets=" + targets.Count.ToString(CultureInfo.InvariantCulture) +
                "|tech_entry_targets=" + techTargets.ToString(CultureInfo.InvariantCulture) +
                "|default_recipe_entry_targets=" + defaultTargets.ToString(CultureInfo.InvariantCulture) +
                "|structural_entry_targets=" + structuralTargets.ToString(CultureInfo.InvariantCulture) +
                "|vendor_candidate_targets=" + vendorTargets.ToString(CultureInfo.InvariantCulture) +
                "|quest_expression_candidate_targets=" + questTargets.ToString(CultureInfo.InvariantCulture) +
                "|any_candidate_targets=" + anyTargets.ToString(CultureInfo.InvariantCulture) +
                "|uncovered_targets=" + uncoveredTargets.ToString(CultureInfo.InvariantCulture));

            Logger.LogInfo("AR_EXPOSURE_DONE|probe=0.2.0");
        }

        private static bool IsPickerCompatible(
            object craft,
            Dictionary<string, object> itemById)
        {
            string[] needs = ItemIds(Get(craft, "needs") as IList).ToArray();
            if (needs.Length != 2 && needs.Length != 3)
                return false;

            string[] expected = { "Powder", "Fluid", "Essence" };
            HashSet<string> seen = new HashSet<string>(StringComparer.Ordinal);

            for (int i = 0; i < needs.Length; i++)
            {
                if (!seen.Add(needs[i]))
                    return false;

                object def;
                if (!itemById.TryGetValue(needs[i], out def) || def == null)
                    return false;

                string type = Str(Get(def, "alch_type"));
                if (type != expected[i] && type != "Universal")
                    return false;
            }

            return true;
        }

        private static bool IsDownstreamConsumerCraft(object craft)
        {
            string type = Str(Get(craft, "craft_type"));
            return type != "MixedCraft"
                   && type != "AlchemyDecompose"
                   && type != "Survey";
        }

        private static bool NeedsItem(object craft, string itemId)
        {
            return ItemIds(Get(craft, "needs") as IList)
                .Any(delegate(string x) { return string.Equals(x, itemId, StringComparison.Ordinal); });
        }

        private static Dictionary<string, object> IndexById(IList list)
        {
            Dictionary<string, object> result =
                new Dictionary<string, object>(StringComparer.Ordinal);

            if (list == null)
                return result;

            foreach (object obj in list)
            {
                string id = Id(obj);
                if (id.Length > 0 && !result.ContainsKey(id))
                    result[id] = obj;
            }

            return result;
        }

        private static bool StaticVendorCanStock(object vendor, object itemDef, string itemId)
        {
            HashSet<string> itemTypes = StringSet(Get(itemDef, "product_types") as IList);
            HashSet<string> vendorTypes = StringSet(Get(vendor, "product_types") as IList);
            if (itemTypes.Count == 0 || vendorTypes.Count == 0 || !itemTypes.Overlaps(vendorTypes))
                return false;

            int productTier = Int(Get(itemDef, "product_tier"));
            int baseCount = Int(Get(itemDef, "base_count"));

            for (int tier = Math.Max(1, productTier); tier <= 3; tier++)
            {
                if (VendorBlocksSelling(vendor, itemId, tier))
                    continue;

                int count = baseCount;
                IList modifiers = Get(vendor, "count_modificators") as IList;
                if (modifiers != null)
                {
                    foreach (object modifier in modifiers)
                    {
                        if (modifier == null)
                            continue;

                        if (string.Equals(Str(Get(modifier, "item_name")), itemId, StringComparison.Ordinal)
                            && Int(Get(modifier, "tier")) <= tier)
                        {
                            count = Int(Get(modifier, "base_count"));
                        }
                    }
                }

                if (count != 0)
                    return true;
            }

            return false;
        }

        private static bool VendorBlocksSelling(object vendor, string itemId, int tier)
        {
            IList list = Get(vendor, "not_selling") as IList;
            if (list == null)
                return false;

            foreach (object modifier in list)
            {
                if (modifier == null
                    || !string.Equals(Str(Get(modifier, "item_name")), itemId, StringComparison.Ordinal))
                {
                    continue;
                }

                int blockedTier = Int(Get(modifier, "tier"));
                if (blockedTier < 1 || blockedTier == tier)
                    return true;
            }

            return false;
        }

        private static bool QuestReferencesItem(object quest, string itemId)
        {
            if (ExpressionReferencesItem(Get(quest, "start_trigger"), itemId)
                || ExpressionReferencesItem(Get(quest, "success_trigger"), itemId)
                || ExpressionReferencesItem(Get(quest, "fail_trigger"), itemId))
            {
                return true;
            }

            foreach (string field in new[] { "success_expressions", "fail_expressions" })
            {
                IList list = Get(quest, field) as IList;
                if (list == null)
                    continue;

                foreach (object expression in list)
                {
                    if (ExpressionReferencesItem(expression, itemId))
                        return true;
                }
            }

            return false;
        }

        private static bool ExpressionReferencesItem(object expression, string itemId)
        {
            string raw = Str(Get(expression, "_expression"));
            if (raw.Length == 0)
                return false;

            return raw.IndexOf(""" + itemId + """, StringComparison.Ordinal) >= 0;
        }

        private static HashSet<string> StringSet(IList list)
        {
            HashSet<string> result = new HashSet<string>(StringComparer.Ordinal);
            if (list == null)
                return result;

            foreach (object value in list)
            {
                string text = Convert.ToString(value, CultureInfo.InvariantCulture) ?? string.Empty;
                if (text.Length > 0)
                    result.Add(text);
            }

            return result;
        }

        private static int Int(object obj)
        {
            try
            {
                return obj == null ? 0 : Convert.ToInt32(obj, CultureInfo.InvariantCulture);
            }
            catch
            {
                return 0;
            }
        }

        private static bool IsSuccessFormula(object craft)
        {
            string id = Id(craft);
            return id.StartsWith("mix:", StringComparison.Ordinal)
                   && id.IndexOf("goo", StringComparison.Ordinal) < 0
                   && id.IndexOf(":_:", StringComparison.Ordinal) < 0;
        }

        private static string StationId(object craft)
        {
            string[] parts = Id(craft).Split(':');
            return parts.Length > 1 ? parts[1] : string.Empty;
        }

        private static string PrimaryOutput(object craft)
        {
            IList output = Get(craft, "output") as IList;
            if (output == null)
                return string.Empty;

            foreach (object item in output)
            {
                string id = Id(item);
                if (id.Length > 0 && !TechOutputs.Contains(id))
                    return id;
            }

            return string.Empty;
        }

        private static IEnumerable<string> ItemIds(IList list)
        {
            if (list == null)
                yield break;

            foreach (object item in list)
            {
                string id = Id(item);
                if (id.Length > 0 && !TechOutputs.Contains(id))
                    yield return id;
            }
        }

        private static Dictionary<string, string> Symbols(IList<string> values, string prefix)
        {
            Dictionary<string, string> result =
                new Dictionary<string, string>(StringComparer.Ordinal);

            for (int i = 0; i < values.Count; i++)
                result[values[i]] =
                    prefix + (i + 1).ToString("D4", CultureInfo.InvariantCulture);

            return result;
        }

        private bool BindGame()
        {
            if (_gameAssembly != null)
                return true;

            _gameAssembly = AppDomain.CurrentDomain.GetAssemblies()
                .FirstOrDefault(delegate(Assembly a)
                {
                    return a.GetName().Name == "Assembly-CSharp";
                });

            return _gameAssembly != null;
        }

        private Type GameType(string name)
        {
            if (_gameAssembly == null)
                return null;

            Type direct = _gameAssembly.GetType(name, false);
            if (direct != null)
                return direct;

            try
            {
                return _gameAssembly.GetTypes()
                    .FirstOrDefault(delegate(Type t)
                    {
                        return t != null && t.Name == name;
                    });
            }
            catch (ReflectionTypeLoadException ex)
            {
                return ex.Types.FirstOrDefault(delegate(Type t)
                {
                    return t != null && t.Name == name;
                });
            }
        }

        private static object Get(object obj, string name)
        {
            if (obj == null)
                return null;

            for (Type type = obj.GetType(); type != null; type = type.BaseType)
            {
                FieldInfo field = type.GetField(name, Inst);
                if (field != null)
                    return field.GetValue(obj);

                PropertyInfo property = type.GetProperty(name, Inst);
                if (property != null && property.CanRead)
                    return property.GetValue(obj, null);
            }

            return null;
        }

        private static object GetStatic(Type type, string name)
        {
            if (type == null)
                return null;

            for (Type current = type; current != null; current = current.BaseType)
            {
                FieldInfo field = current.GetField(name, Stat);
                if (field != null)
                    return field.GetValue(null);

                PropertyInfo property = current.GetProperty(name, Stat);
                if (property != null && property.CanRead)
                    return property.GetValue(null, null);
            }

            return null;
        }

        private static int Count(IList list)
        {
            return list == null ? 0 : list.Count;
        }

        private static string Id(object obj)
        {
            return Get(obj, "id") as string ?? string.Empty;
        }

        private static string Str(object obj)
        {
            return Convert.ToString(obj, CultureInfo.InvariantCulture) ?? string.Empty;
        }

        private static bool Bool(object obj)
        {
            try
            {
                return obj != null && Convert.ToBoolean(obj, CultureInfo.InvariantCulture);
            }
            catch
            {
                return false;
            }
        }

        private static string Esc(string value)
        {
            if (string.IsNullOrEmpty(value))
                return string.Empty;

            return value
                .Replace("\\", "\\\\")
                .Replace("|", "\\|")
                .Replace("\r", " ")
                .Replace("\n", " ");
        }
    }
}
