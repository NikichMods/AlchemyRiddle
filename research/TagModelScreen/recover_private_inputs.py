"""Recover private screen inputs from verified local assets and accepted runtime log.

Research only. Requires UnityPy. Never prints ingredient/target identities or
recipes. Raw game payloads stay in memory; derived inputs must stay outside Git.
"""
import argparse
import collections
import hashlib
import json
import re
import struct
from pathlib import Path

import UnityPy

ASSET_HASH = '215c7981901a4b72d5db717666ba47ad3cc032527c95f58dc39d8af1293a69ca'
LOG_HASH = 'd4d5817fb9a00917188f0c740a60c2e567f6c8e3e299ed27a158c84e5cd33094'
ROOT = Path(__file__).resolve().parents[2]
TAG_NAMES = dict(zip(
    ['Растение', 'Труп', 'Минерал', 'Насекомое', 'Животное', 'Рыба', 'Слизь', 'Вода'],
    ['Plant', 'Corpse', 'Mineral', 'Insect', 'Animal', 'Fish', 'Slime', 'Water']))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def goo(identifier):
    return 'goo_' + re.sub(r'^alchemy_[123]_|^powder_|^drop_', '', identifier)


def localization(raw):
    # GJL's serialized fields: MonoBehaviour header, id, four string lists.
    pos = 28
    def string():
        nonlocal pos
        n = struct.unpack_from('<I', raw, pos)[0]
        pos += 4
        require(n <= len(raw) - pos, 'GJL string exceeds object')
        value = raw[pos:pos+n].decode('utf-8')
        pos = (pos + n + 3) & ~3
        return value
    def array():
        nonlocal pos
        n = struct.unpack_from('<I', raw, pos)[0]
        pos += 4
        require(n < 100000, 'GJL array exceeds bound')
        return [string() for _ in range(n)]
    require(string() == 'lng_ru' and string() == 'ru', 'Wrong GJL object')
    ids, texts, aliases1, aliases2 = array(), array(), array(), array()
    require(pos == len(raw) and len(ids) == len(texts), 'Incomplete GJL parsing')
    require(len(aliases1) == len(aliases2), 'Invalid GJL aliases')
    return dict(zip(ids, texts))


def recover(asset, log, output):
    require(not output.resolve().is_relative_to(ROOT), 'Private output must be outside repository')
    require(hashlib.sha256(asset.read_bytes()).hexdigest() == ASSET_HASH, 'Unverified assets')
    require(hashlib.sha256(log.read_bytes()).hexdigest() == LOG_HASH, 'Unverified runtime capture')
    env = UnityPy.load(str(asset))
    objects = {}
    for obj in env.objects:
        if obj.type.name == 'MonoBehaviour':
            head = obj.parse_monobehaviour_head()
            if head.m_Name in ('game_data', 'lng_ru'):
                objects[head.m_Name] = obj.get_raw_data()
    require(len(objects) == 2, 'Required serialized objects absent')
    names = localization(objects['lng_ru'])
    raw = objects['game_data']
    strings = [(m.start(), m.group().decode()) for m in
               re.finditer(rb'[a-zA-Z_][a-zA-Z0-9_:.@ -]{1,130}', raw)
               if m.start() >= 4 and int.from_bytes(raw[m.start()-4:m.start()], 'little') == len(m.group())]
    keys = [value for _, value in strings if value.startswith('mix:')]
    require(len(keys) == len(set(keys)) == 509, 'Static recipe key population mismatch')
    rows = collections.defaultdict(list)
    for line in log.read_text(encoding='utf-8-sig').splitlines():
        match = re.search(r'\b(AR_ITEM|AR_GOO_MAP|AR_RECIPE)\|(.+)$', line)
        if match:
            rows[match[1]].append(dict(field.split('=', 1) for field in match[2].split('|')))
    expected_goo = {(r['from'], r['to']) for r in rows['AR_GOO_MAP']}
    tokens = {x for key in keys for x in key.split(':')[2:] if x and x != '_'}
    # One exceptional key contains a token absent from actual needs. Identify
    # it by the entire 57-row runtime map, rather than guessing its meaning.
    joins = []
    for omitted in tokens:
        needs = tokens - {omitted}
        population = sorted(needs | {goo(x) for x in needs})
        symbols = {x: 'N{:04}'.format(i+1) for i, x in enumerate(population)}
        if len(population) == 79 and {(symbols[x], symbols[goo(x)]) for x in needs} == expected_goo:
            joins.append((omitted, symbols))
    require(len(joins) == 1, 'No unique complete symbol/goo join')
    omitted, symbols = joins[0]
    reverse = {v: k for k, v in symbols.items()}
    types = {r['item']: r['alchemy_type'] for r in rows['AR_ITEM']}
    success_keys = sorted(k for k in keys if 'goo' not in k and ':_:' not in k)
    success_log = [r for r in rows['AR_RECIPE'] if r['kind'] == 'success']
    require(len(success_keys) == len(success_log) == 44, 'Success population mismatch')
    for key, record in zip(success_keys, success_log):
        expected = [x for x in key.split(':')[2:] if x and x != omitted]
        actual = [reverse[x] for x in record['needs'].split(',') if x]
        require(expected == actual, 'Static/runtime exact ingredient sequence mismatch')
    ordinary = [r for r in success_log if all(
        types[x] in ('Universal', ['Powder','Fluid','Essence'][i])
        for i,x in enumerate(r['needs'].split(',')))]
    require(len(ordinary) == 43, 'Ordinary population mismatch')
    participants = {x for r in ordinary for x in r['needs'].split(',')}
    canonical = (ROOT / 'docs/DESIGN_RESEARCH.md').read_text(encoding='utf-8')
    section = canonical.split('The fixed assignment used for the accepted screen was:')[1].split('### Signature diversity')[0]
    assignment = {}; assignment_types = {}
    for line in section.splitlines():
        parts = [x.strip() for x in line.split('|')]
        if len(parts) == 5 and parts[1] in ('Universal','Powder','Fluid','Essence'):
            assignment[parts[2]] = {TAG_NAMES[t.strip()] for t in parts[3].split(',')}
            assignment_types[parts[2]] = parts[1]
    require(len(assignment) == 35, 'Canonical base property population mismatch')
    ingredients = []
    for symbol in sorted(participants):
        identifier = reverse[symbol]
        localized_id = identifier
        if localized_id not in names:
            qualified = [k for k in names if ':' in k and k.rsplit(':',1)[1] == identifier]
            require(len(qualified) == 1, 'Ambiguous colon-qualified reagent identity')
            localized_id = qualified[0]
        require(localized_id in names and names[localized_id] in assignment,
                'Canonical/localized reagent identity mismatch: ' + identifier)
        tags = set(assignment[names[localized_id]])
        require(types[symbol] == assignment_types[names[localized_id]], 'Canonical/runtime reagent role mismatch')
        if identifier.startswith('alchemy_') and identifier[10:] in ('d_blue','d_green','d_violet'):
            require(any(f in names[identifier] for f in ('ускорен','здоров','смерт')), 'Dark family localization mismatch')
            tags.add('Dark')
        if identifier.startswith('alchemy_') and identifier[10:] in ('yellow','d_violet'):
            tags.add('Organ')
        ingredients.append(dict(name=symbol, type=types[symbol], tags=sorted(tags)))
    require(collections.Counter(len(r['tags']) for r in ingredients) == {1:12,2:11,3:8,4:4}, 'Accepted property distribution mismatch')
    require(sum('Dark' in r['tags'] for r in ingredients)==9 and sum('Organ' in r['tags'] for r in ingredients)==6, 'Overlay membership count mismatch')
    require({role:len({tuple(r['tags']) for r in ingredients if r['type']==role})
             for role in ('Powder','Fluid','Essence','Universal')} ==
            dict(Powder=12,Fluid=8,Essence=6,Universal=4), 'Accepted role signature counts mismatch')
    # Bound Organ validation to explicit direct decomposition records. Their
    # output must be the next reagent identifier before the next craft key.
    organ_outputs = set()
    for i, (_, value) in enumerate(strings):
        if value.startswith('alch:') and value.split(':')[-1] in ('brain','brain_dark','heart','heart_dark','intestine','intestine_dark'):
            after = [s for _,s in strings[i+1:i+6]]
            require(value.split(':')[-1] in after, 'Organ source witness absent')
            outputs = [s for s in after if s.startswith('alchemy_')]
            require(len(outputs)==1, 'Ambiguous organ output witness')
            organ_outputs.add(outputs[0])
    require(organ_outputs == {reverse[r['name']] for r in ingredients if 'Organ' in r['tags']}, 'Organ source overlay mismatch')
    formula_rows = []
    for r in ordinary:
        parts = r['needs'].split(',')
        formula_rows.append(dict(output=r['output'], **dict(zip(['powder','fluid','essence'],parts))))
    positions = {s:i for i,(_,s) in enumerate(strings) if s.startswith('mix:')}
    all_runtime = rows['AR_RECIPE']
    require(len(all_runtime) == 509, 'Incomplete runtime recipe population')
    # The recipe record's first output follows station and its recorded needs.
    # Treat that narrow positional extraction as a candidate until every one
    # of the 509 output symbols agrees with the independent loaded-runtime log.
    static_outputs = [strings[positions[k]+2+int(r['arity'])][1]
                      for k,r in zip(sorted(keys),all_runtime)]
    out_symbols = {s:'O{:04}'.format(i+1) for i,s in enumerate(sorted(set(static_outputs)))}
    require(len(out_symbols)==57 and all(out_symbols[s]==r['output']
            for s,r in zip(static_outputs,all_runtime)), 'Static/runtime output identity mismatch')
    named_outputs = {out_symbols[s]:names.get(s,'') for s in static_outputs}
    decorative = {s for s,n in named_outputs.items() if 'краска' in n.lower()
                  and n not in ('Белая краска','Черная краска','Чёрная краска')}
    core = [r for r in formula_rows if 'essence' not in r and r['output'] not in decorative]
    require(len(decorative)==8 and len(core)==16 and len({r['output'] for r in core})==10,
            'Canonical decorative/core scope mismatch')
    require(len({r['powder'] for r in core})==12 and len({r['fluid'] for r in core})==9,
            'Core candidate population mismatch')
    output.mkdir(parents=True, exist_ok=True)
    for arity in (2,3):
        data=dict(ingredients=ingredients, formulas=[r for r in formula_rows if len(r)==arity+1])
        (output / ('ordinary-{}.json'.format(arity))).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    (output/'core-2.json').write_text(json.dumps(dict(ingredients=ingredients,formulas=core),indent=2),encoding='utf-8')
    result=dict(assetSha256=ASSET_HASH,logSha256=LOG_HASH,exactSuccessRowsCompared=44,
                gooPairsCompared=57,ordinaryFormulas=43,propertyCards=35,darkCards=9,organCards=6,
                propertyHistogram={str(k):v for k,v in sorted(collections.Counter(len(r['tags']) for r in ingredients).items())},
                exactOutputRowsCompared=509,twoCoreFormulas=16,twoCoreOutputs=10)
    (output/'join-validation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('asset',type=Path)
    parser.add_argument('log',type=Path)
    parser.add_argument('private_output',type=Path)
    args=parser.parse_args()
    recover(args.asset,args.log,args.private_output)
