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
        public const string Version = "0.3.0";

        private static readonly BindingFlags Inst =
            BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic;
        private static readonly BindingFlags Stat =
            BindingFlags.Static | BindingFlags.Public | BindingFlags.NonPublic;

        private static readonly HashSet<string> TechOutputs =
            new HashSet<string>(
                new[] { "r", "g", "b", "v", "gratitude_points" },
                StringComparer.Ordinal);

        private Assembly _gameAssembly;
        private Type _gjlType;
        private MethodInfo _localize;
        private bool _dumped;

        private void Awake()
        {
            Logger.LogInfo("AlchemyRiddle Corpus Probe 0.3.0 loaded. Read-only property/provenance research probe.");
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
                                InitLocalization();
                                Dump(balance);
                            }
                            catch (Exception ex)
                            {
                                Logger.LogError("AR_PROPERTY_ERROR|" + Esc(ex.ToString()));
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
            IList objects = Get(balance, "objs_data") as IList;
            IList vendors = Get(balance, "vendors_data") as IList;
            IList objectCrafts = Get(balance, "craft_obj_data") as IList;
            IList techs = Get(balance, "techs_data") as IList;
            IList quests = Get(balance, "quests_data") as IList;

            if (items == null || crafts == null || objects == null || vendors == null
                || objectCrafts == null || techs == null || quests == null)
            {
                throw new InvalidOperationException(
                    "Required loaded GameBalance lists are not available.");
            }

            Dictionary<string, object> itemById = IndexById(items);

            List<object> mixedAlchemy = new List<object>();
            foreach (object craft in crafts)
            {
                if (craft == null)
                    continue;

                if (!string.Equals(Str(Get(craft, "craft_type")), "MixedCraft", StringComparison.Ordinal))
                    continue;

                string id = Id(craft);
                if (id.StartsWith("mix:mf_alchemy", StringComparison.Ordinal))
                    mixedAlchemy.Add(craft);
            }

            List<object> ordinarySuccess = mixedAlchemy
                .Where(IsSuccessFormula)
                .Where(delegate(object c) { return IsPickerCompatible(c, itemById); })
                .ToList();

            List<string> ingredientIds = ordinarySuccess
                .SelectMany(delegate(object c) { return ItemIds(Get(c, "needs") as IList); })
                .Distinct(StringComparer.Ordinal)
                .ToList();

            List<string> targetIds = ordinarySuccess
                .Select(PrimaryOutput)
                .Where(delegate(string x) { return x.Length > 0; })
                .Distinct(StringComparer.Ordinal)
                .ToList();

            Dictionary<string, string> ingredientSymbols =
                PresentationSymbols(ingredientIds, itemById, "P");
            Dictionary<string, string> targetSymbols =
                PresentationSymbols(targetIds, itemById, "Q");

            Type itemDefinitionType = GameType("ItemDefinition");
            MethodInfo gooMethod = itemDefinitionType == null
                ? null
                : itemDefinitionType.GetMethod(
                    "GetGooFromAlchemyIngridient",
                    BindingFlags.Static | BindingFlags.Public | BindingFlags.NonPublic,
                    null,
                    new[] { typeof(string) },
                    null);

            Logger.LogInfo(
                "AR_PROPERTY_BEGIN|probe=0.3.0|target=GraveyardKeeper-1.407|source=loaded-GameBalance");
            Logger.LogInfo(
                "AR_PROPERTY_SOURCE|decompile_reference=Kupie/GYK_DECOMP@6abf79199d92482af1c7573870dd9a20ec2270b9");
            Logger.LogInfo(
                "AR_PROPERTY_SUMMARY" +
                "|ordinary_formulas=" + ordinarySuccess.Count.ToString(CultureInfo.InvariantCulture) +
                "|ingredients=" + ingredientIds.Count.ToString(CultureInfo.InvariantCulture) +
                "|targets=" + targetIds.Count.ToString(CultureInfo.InvariantCulture) +
                "|formula_rows_logged=0");

            foreach (KeyValuePair<string, string> pair in
                ingredientSymbols.OrderBy(delegate(KeyValuePair<string, string> x) { return x.Value; }, StringComparer.Ordinal))
            {
                string itemId = pair.Key;
                string symbol = pair.Value;
                object def;
                itemById.TryGetValue(itemId, out def);
                if (def == null)
                    continue;

                string gooId = gooMethod == null
                    ? string.Empty
                    : Str(gooMethod.Invoke(null, new object[] { itemId }));

                object gooDef;
                itemById.TryGetValue(gooId, out gooDef);

                List<object> producers = ProducerCrafts(crafts, itemId);
                List<object> drops = DropObjects(objects, itemId);
                List<object> sellerDefs = VendorCandidates(vendors, def, itemId);

                Logger.LogInfo(
                    "AR_PROPERTY_ITEM" +
                    "|item=" + symbol +
                    "|name=" + Esc(ItemName(def)) +
                    "|description=" + Esc(ItemDescription(def)) +
                    "|icon=" + Esc(ItemIcon(def)) +
                    "|alchemy_type=" + Esc(Str(Get(def, "alch_type"))) +
                    "|goo=" + Esc(gooId) +
                    "|goo_name=" + Esc(gooDef == null ? Localize(gooId) : ItemName(gooDef)) +
                    "|tooltip_stations=" + Esc(string.Join(";", TooltipStations(def))) +
                    "|product_types=" + Esc(string.Join(";", Strings(Get(def, "product_types") as IList))) +
                    "|product_tier=" + Int(Get(def, "product_tier")).ToString(CultureInfo.InvariantCulture) +
                    "|base_price=" + Float(Get(def, "base_price")).ToString("0.###", CultureInfo.InvariantCulture) +
                    "|base_count=" + Int(Get(def, "base_count")).ToString(CultureInfo.InvariantCulture) +
                    "|producer_crafts=" + producers.Count.ToString(CultureInfo.InvariantCulture) +
                    "|drop_sources=" + drops.Count.ToString(CultureInfo.InvariantCulture) +
                    "|vendor_candidates=" + sellerDefs.Count.ToString(CultureInfo.InvariantCulture));

                foreach (object craft in producers
                    .OrderBy(delegate(object x) { return Str(Get(x, "craft_type")); }, StringComparer.Ordinal)
                    .ThenBy(Id, StringComparer.Ordinal))
                {
                    string craftType = Str(Get(craft, "craft_type"));
                    string[] needs = ItemIds(Get(craft, "needs") as IList)
                        .Select(delegate(string x) { return DisplayItemName(x, itemById); })
                        .ToArray();

                    Logger.LogInfo(
                        "AR_PROPERTY_PRODUCER" +
                        "|item=" + symbol +
                        "|kind=" + Esc(craftType) +
                        "|stations=" + Esc(string.Join(";", CraftStations(craft))) +
                        "|needs=" + Esc(string.Join(";", needs)) +
                        "|hidden=" + Bool(Get(craft, "hidden")).ToString().ToLowerInvariant() +
                        "|needs_unlock=" + Bool(Get(craft, "needs_unlock")).ToString().ToLowerInvariant() +
                        "|dont_show_in_hint=" + Bool(Get(craft, "dont_show_in_hint")).ToString().ToLowerInvariant() +
                        "|craft_time_expr=" + Esc(ExpressionRaw(Get(craft, "craft_time"))) +
                        "|energy_expr=" + Esc(ExpressionRaw(Get(craft, "energy"))));

                    if (craftType == "AlchemyDecompose")
                    {
                        string sourceId = ItemIds(Get(craft, "needs") as IList).FirstOrDefault() ?? string.Empty;
                        object sourceDef;
                        itemById.TryGetValue(sourceId, out sourceDef);

                        if (sourceDef != null)
                        {
                            List<object> sourceProducers = ProducerCrafts(crafts, sourceId);
                            List<object> sourceDrops = DropObjects(objects, sourceId);
                            List<object> sourceSellers = VendorCandidates(vendors, sourceDef, sourceId);
                            object survey = Invoke(sourceDef, "GetSurveyCraft");

                            Logger.LogInfo(
                                "AR_PROPERTY_DECOMP_SOURCE" +
                                "|item=" + symbol +
                                "|source_name=" + Esc(ItemName(sourceDef)) +
                                "|source_description=" + Esc(ItemDescription(sourceDef)) +
                                "|source_icon=" + Esc(ItemIcon(sourceDef)) +
                                "|source_tooltip_stations=" + Esc(string.Join(";", TooltipStations(sourceDef))) +
                                "|source_survey_exists=" + (survey != null).ToString().ToLowerInvariant() +
                                "|source_producer_stations=" + Esc(string.Join(";", sourceProducers.SelectMany(CraftStations).Distinct(StringComparer.Ordinal))) +
                                "|source_drop_objects=" + Esc(string.Join(";", sourceDrops.Select(ObjectLabel).Distinct(StringComparer.Ordinal))) +
                                "|source_vendor_candidates=" + sourceSellers.Count.ToString(CultureInfo.InvariantCulture));
                        }
                    }
                }

                foreach (object obj in drops.OrderBy(Id, StringComparer.Ordinal))
                {
                    Logger.LogInfo(
                        "AR_PROPERTY_DROP" +
                        "|item=" + symbol +
                        "|object=" + Esc(ObjectLabel(obj)) +
                        "|object_type=" + Esc(Str(Get(obj, "type"))) +
                        "|zone_id=" + Esc(Str(Get(obj, "zone_id"))));
                }

                foreach (object vendor in sellerDefs.OrderBy(Id, StringComparer.Ordinal))
                {
                    Logger.LogInfo(
                        "AR_PROPERTY_VENDOR" +
                        "|item=" + symbol +
                        "|vendor=" + Esc(Localize(Id(vendor))) +
                        "|start_tier=" + Int(Get(vendor, "start_tire")).ToString(CultureInfo.InvariantCulture));
                }
            }

            Dictionary<string, object> craftById = IndexById(crafts);
            Dictionary<string, object> objectCraftById = IndexById(objectCrafts);

            foreach (KeyValuePair<string, string> pair in
                targetSymbols.OrderBy(delegate(KeyValuePair<string, string> x) { return x.Value; }, StringComparer.Ordinal))
            {
                string target = pair.Key;
                string symbol = pair.Value;
                object def;
                itemById.TryGetValue(target, out def);

                HashSet<string> ordinaryConsumers = new HashSet<string>(StringComparer.Ordinal);
                HashSet<string> blueprintConsumers = new HashSet<string>(StringComparer.Ordinal);
                HashSet<string> defaultVisibleConsumers = new HashSet<string>(StringComparer.Ordinal);
                HashSet<string> techVisibleConsumers = new HashSet<string>(StringComparer.Ordinal);
                HashSet<string> techPublicNodes = new HashSet<string>(StringComparer.Ordinal);
                HashSet<string> techGatedNodes = new HashSet<string>(StringComparer.Ordinal);

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
                        if (raw.Length == 0 || raw[0] == '@')
                            continue;

                        object consumer;
                        if (!craftById.TryGetValue(raw, out consumer))
                            objectCraftById.TryGetValue(raw, out consumer);

                        if (consumer == null || Bool(Get(consumer, "hidden")) || !NeedsItem(consumer, target))
                            continue;

                        techVisibleConsumers.Add(raw);
                        if (techId.Length > 0)
                        {
                            if (Bool(Get(tech, "hidden")) || Bool(Get(tech, "invisible")))
                                techGatedNodes.Add(techId);
                            else
                                techPublicNodes.Add(techId);
                        }
                    }
                }

                int vendorCandidates = def == null ? 0 : VendorCandidates(vendors, def, target).Count;
                int questRefs = 0;
                foreach (object quest in quests)
                {
                    if (quest != null && Bool(Get(quest, "quest_visible")) && QuestReferencesItem(quest, target))
                        questRefs++;
                }

                Logger.LogInfo(
                    "AR_PROPERTY_TARGET" +
                    "|target=" + symbol +
                    "|name=" + Esc(def == null ? string.Empty : ItemName(def)) +
                    "|description=" + Esc(def == null ? string.Empty : ItemDescription(def)) +
                    "|icon=" + Esc(def == null ? string.Empty : ItemIcon(def)) +
                    "|formulas=" + ordinarySuccess.Count(delegate(object c)
                    {
                        return string.Equals(PrimaryOutput(c), target, StringComparison.Ordinal);
                    }).ToString(CultureInfo.InvariantCulture) +
                    "|ordinary_consumers=" + ordinaryConsumers.Count.ToString(CultureInfo.InvariantCulture) +
                    "|blueprint_consumers=" + blueprintConsumers.Count.ToString(CultureInfo.InvariantCulture) +
                    "|default_visible_consumers=" + defaultVisibleConsumers.Count.ToString(CultureInfo.InvariantCulture) +
                    "|tech_visible_consumers=" + techVisibleConsumers.Count.ToString(CultureInfo.InvariantCulture) +
                    "|tech_public_nodes=" + techPublicNodes.Count.ToString(CultureInfo.InvariantCulture) +
                    "|tech_gated_nodes=" + techGatedNodes.Count.ToString(CultureInfo.InvariantCulture) +
                    "|vendor_static_stock_candidates=" + vendorCandidates.ToString(CultureInfo.InvariantCulture) +
                    "|visible_quest_expression_refs=" + questRefs.ToString(CultureInfo.InvariantCulture) +
                    "|product_tier=" + Int(Get(def, "product_tier")).ToString(CultureInfo.InvariantCulture) +
                    "|base_price=" + Float(Get(def, "base_price")).ToString("0.###", CultureInfo.InvariantCulture));
            }

            Logger.LogInfo(
                "AR_PROPERTY_DONE|probe=0.3.0" +
                "|ingredient_records=" + ingredientIds.Count.ToString(CultureInfo.InvariantCulture) +
                "|target_records=" + targetIds.Count.ToString(CultureInfo.InvariantCulture) +
                "|formula_rows_logged=0");
        }

        private List<object> ProducerCrafts(IList crafts, string itemId)
        {
            List<object> result = new List<object>();
            foreach (object craft in crafts)
            {
                if (craft == null)
                    continue;

                string type = Str(Get(craft, "craft_type"));
                if (type == "MixedCraft" || type == "Survey")
                    continue;

                if (ContainsItem(Get(craft, "output") as IList, itemId))
                    result.Add(craft);
            }
            return result;
        }

        private static List<object> DropObjects(IList objects, string itemId)
        {
            List<object> result = new List<object>();
            foreach (object obj in objects)
            {
                if (obj != null && ContainsItem(Get(obj, "drop_items") as IList, itemId))
                    result.Add(obj);
            }
            return result;
        }

        private List<object> VendorCandidates(IList vendors, object itemDef, string itemId)
        {
            List<object> result = new List<object>();
            if (itemDef == null)
                return result;

            foreach (object vendor in vendors)
            {
                if (vendor != null && StaticVendorCanStock(vendor, itemDef, itemId))
                    result.Add(vendor);
            }
            return result;
        }

        private string[] TooltipStations(object def)
        {
            object details = Invoke(def, "GetItemDetails");
            IList craftsIn = Get(details, "crafts_in") as IList;
            if (craftsIn == null)
                return new string[0];

            return craftsIn.Cast<object>()
                .Where(delegate(object x) { return x != null; })
                .Select(delegate(object x) { return Localize(Id(x)); })
                .Where(delegate(string x) { return x.Length > 0; })
                .Distinct(StringComparer.Ordinal)
                .ToArray();
        }

        private string[] CraftStations(object craft)
        {
            IList stations = Get(craft, "craft_in") as IList;
            if (stations == null)
                return new string[0];

            return Strings(stations)
                .Where(delegate(string x) { return x.Length > 0; })
                .Select(Localize)
                .Distinct(StringComparer.Ordinal)
                .ToArray();
        }

        private string ObjectLabel(object obj)
        {
            string id = Id(obj);
            string localized = Localize(id);
            return string.IsNullOrEmpty(localized) ? id : localized;
        }

        private string DisplayItemName(string id, Dictionary<string, object> itemById)
        {
            object def;
            return itemById.TryGetValue(id, out def) && def != null
                ? ItemName(def)
                : Localize(id);
        }

        private string ItemName(object def)
        {
            return Str(Invoke(def, "GetItemName", true));
        }

        private string ItemDescription(object def)
        {
            return Str(Invoke(def, "GetItemDescription", new object[] { null }));
        }

        private string ItemIcon(object def)
        {
            return Str(Invoke(def, "GetIcon"));
        }

        private static string ExpressionRaw(object expression)
        {
            if (expression == null)
                return string.Empty;

            object raw = Invoke(expression, "GetRawExpressionString");
            return Str(raw);
        }

        private Dictionary<string, string> PresentationSymbols(
            IList<string> ids,
            Dictionary<string, object> itemById,
            string prefix)
        {
            List<string> ordered = ids
                .OrderBy(delegate(string x)
                {
                    object def;
                    return itemById.TryGetValue(x, out def) && def != null
                        ? ItemName(def)
                        : x;
                }, StringComparer.CurrentCulture)
                .ThenBy(delegate(string x)
                {
                    object def;
                    return itemById.TryGetValue(x, out def) && def != null
                        ? ItemIcon(def)
                        : x;
                }, StringComparer.Ordinal)
                .ThenBy(delegate(string x) { return x; }, StringComparer.Ordinal)
                .ToList();

            Dictionary<string, string> result =
                new Dictionary<string, string>(StringComparer.Ordinal);

            for (int i = 0; i < ordered.Count; i++)
                result[ordered[i]] = prefix + (i + 1).ToString("D4", CultureInfo.InvariantCulture);

            return result;
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

        private static bool IsSuccessFormula(object craft)
        {
            string id = Id(craft);
            return id.StartsWith("mix:", StringComparison.Ordinal)
                   && id.IndexOf("goo", StringComparison.Ordinal) < 0
                   && id.IndexOf(":_:", StringComparison.Ordinal) < 0;
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

        private static bool ContainsItem(IList list, string itemId)
        {
            return ItemIds(list)
                .Any(delegate(string x) { return string.Equals(x, itemId, StringComparison.Ordinal); });
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
            return ContainsItem(Get(craft, "needs") as IList, itemId);
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

        private static string[] Strings(IList list)
        {
            if (list == null)
                return new string[0];

            List<string> result = new List<string>();
            foreach (object value in list)
            {
                string text = Convert.ToString(value, CultureInfo.InvariantCulture) ?? string.Empty;
                if (text.Length > 0)
                    result.Add(text);
            }
            return result.ToArray();
        }

        private static HashSet<string> StringSet(IList list)
        {
            return new HashSet<string>(Strings(list), StringComparer.Ordinal);
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

            return raw.IndexOf("\\\"" + itemId + "\\\"", StringComparison.Ordinal) >= 0;
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

        private void InitLocalization()
        {
            foreach (Assembly assembly in AppDomain.CurrentDomain.GetAssemblies())
            {
                Type type = assembly.GetType("GJL", false);
                if (type == null)
                {
                    try
                    {
                        type = assembly.GetTypes().FirstOrDefault(delegate(Type t)
                        {
                            return t != null && t.Name == "GJL";
                        });
                    }
                    catch (ReflectionTypeLoadException ex)
                    {
                        type = ex.Types.FirstOrDefault(delegate(Type t)
                        {
                            return t != null && t.Name == "GJL";
                        });
                    }
                }

                if (type == null)
                    continue;

                MethodInfo method = type.GetMethods(Stat)
                    .FirstOrDefault(delegate(MethodInfo m)
                    {
                        ParameterInfo[] p = m.GetParameters();
                        return m.Name == "L"
                               && m.ReturnType == typeof(string)
                               && p.Length == 1
                               && p[0].ParameterType == typeof(string);
                    });

                if (method != null)
                {
                    _gjlType = type;
                    _localize = method;
                    return;
                }
            }
        }

        private string Localize(string key)
        {
            if (string.IsNullOrEmpty(key) || _gjlType == null || _localize == null)
                return key ?? string.Empty;

            try
            {
                return Str(_localize.Invoke(null, new object[] { key }));
            }
            catch
            {
                return key;
            }
        }

        private static object Invoke(object obj, string name, params object[] args)
        {
            if (obj == null)
                return null;

            for (Type type = obj.GetType(); type != null; type = type.BaseType)
            {
                foreach (MethodInfo method in type.GetMethods(Inst))
                {
                    if (method.Name != name || method.GetParameters().Length != args.Length)
                        continue;

                    try
                    {
                        return method.Invoke(obj, args);
                    }
                    catch (TargetInvocationException)
                    {
                        throw;
                    }
                    catch
                    {
                    }
                }
            }

            return null;
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

        private static float Float(object obj)
        {
            try
            {
                return obj == null ? 0f : Convert.ToSingle(obj, CultureInfo.InvariantCulture);
            }
            catch
            {
                return 0f;
            }
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
