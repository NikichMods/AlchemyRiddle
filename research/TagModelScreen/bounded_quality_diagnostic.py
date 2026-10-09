"""Bounded quality diagnostic; private inputs/certificates, aggregate public output.

Reuses existing TagModelScreen predicates. Structural proxies are review evidence,
not an interest classifier. Query policies cannot inspect hidden outcomes.
"""
import argparse
import collections
import hashlib
import itertools
import json
import math
import random
import time
from pathlib import Path

import two_slot_tag_constraint_screen as two
import progression_variable_field_screen as three
import reasoning_diversity_screen as reasoning

SEED = 20261007
ROOT = Path(__file__).resolve().parents[2]


def edges(t):
    return (('PF',t[0],t[1]),('FE',t[1],t[2]))


def route(triples, live, priors, oracle, seed):
    """Selection uses public state; oracle is called only after choosing an edge."""
    known = dict.fromkeys(priors, True)
    history = []
    rng = random.Random(seed)
    while True:
        survivors = [t for i,t in enumerate(triples) if live >> i & 1
                     and all(known.get(e) is not False for e in edges(t))]
        certified = [t for t in survivors if all(known.get(e) is True for e in edges(t))]
        if certified:
            return dict(tests=len(history),remaining=len(survivors),certified=len(certified),
                        success=True,negativeTests=sum(not h['stable'] for h in history),
                        certifyingTests=sum(h['stable'] for h in history),
                        orientations=sorted({h['edge'][0] for h in history}),history=history)
        candidates = {e for t in survivors for e in edges(t) if e not in known}
        if not candidates:
            return dict(tests=len(history),remaining=len(survivors),certified=0,
                        success=False,history=history)
        scores = {}
        for e in sorted(candidates):
            affected = [t for t in survivors if e in edges(t)]
            support = sum(any(known.get(x) is True for x in edges(t)) for t in affected)
            scores[e] = (min(len(affected),len(survivors)-len(affected)),support)
        best = max(scores.values())
        query = rng.choice([e for e in sorted(candidates) if scores[e] == best])
        outcome = oracle(query)
        known[query] = outcome
        history.append(dict(edge=query,stable=outcome,affected=sum(query in edges(t) for t in survivors)))


def selection(formulas,tags,pools,seed):
    rng = random.Random(seed)
    ordered = sorted(formulas,key=lambda x:(x['output'],tuple(x[k] for k in ('powder','fluid','essence') if k in x)))
    prevalence=collections.Counter(t for pool in pools for item in pool for t in tags[item])
    def components(r):return tuple(r[k] for k in ('powder','fluid','essence') if k in r)
    richness=lambda r:sum(len(tags[x]) for x in components(r))
    rarity=lambda r:min(prevalence[t] for x in components(r) for t in tags[x])
    result=[]
    for label,key,maximum in [('simple',richness,False),('rich',richness,True),('rare',rarity,False)]:
        remaining=[r for r in ordered if r not in [x[1] for x in result]]
        extreme=(max if maximum else min)(key(r) for r in remaining)
        r=rng.choice([r for r in remaining if key(r)==extreme])
        result.append((label,r))
    return result


def intersects(masks,full):
    for mask in masks:full &= mask
    return full


def scope(mask,tuples):
    active=[]
    for slot in range(len(tuples[0])):
        groups=collections.defaultdict(set)
        for i,t in enumerate(tuples):groups[t[:slot]+t[slot+1:]].add(bool(mask>>i&1))
        if any(len(v)>1 for v in groups.values()):active.append(slot)
    return active


def summarize_package(clues,combo,tuples,tags):
    chosen=[clues[i] for i in combo]
    masks=[c[2] for c in chosen];full=(1<<len(tuples))-1
    scopes=[scope(m,tuples) for m in masks]
    derived=constant_counts=unique_endpoints=immediate=0
    for ci,(family,spec,mask) in enumerate(chosen):
        if family in ('count','count_mixed'):
            role_tags = [spec[1]]*len(tuples[0]) if family=='count' else spec[1]
            constant_counts+=sum(len({tag in tags[t[s]] for t in tuples})==1
                                 for s,tag in enumerate(role_tags))
        if family.startswith('imp'):
            if spec[0]=='imp_pf':a,b,ta,tb=0,1,spec[1],spec[2]
            elif spec[0]=='imp_fp':a,b,ta,tb=1,0,spec[1],spec[2]
            else:_,a,ta,b,tb=spec[:5]
            unique_endpoints+=sum(len({t[s] for t in tuples if tag in tags[t[s]]})==1 for s,tag in [(a,ta),(b,tb)])
            other=intersects([m for j,m in enumerate(masks) if j!=ci],full)
            if all(ta in tags[t[a]] for i,t in enumerate(tuples) if other>>i&1):
                handed=any(scopes[j]==[a] and all(ta in tags[t[a]] for i,t in enumerate(tuples) if masks[j]>>i&1)
                           for j in range(len(chosen)) if j!=ci)
                if handed:immediate+=1
                else:derived+=1
    families=[c[0] for c in chosen]
    return dict(clues=len(chosen),families=families,effectiveScopes=scopes,
                constantCountTerms=constant_counts,derivedAntecedents=derived,
                immediatelyHandedAntecedents=immediate,uniqueConditionalEndpoints=unique_endpoints,
                crossSlotClauses=sum(len(s)>1 for s in scopes),
                controlProxy=all(len(s)<=1 for s in scopes) or all(f in ('count','count_mixed') for f in families))


def package_samples(clues,rng):
    # Half the fixed combination budget seeks the required flat/repeated control.
    simple=[i for i,c in enumerate(clues) if c[0] in ('literal','count')]
    seen=set();result=[]
    for population in (simple,list(range(len(clues)))):
        added=0
        for _ in range(2048):
            if added==128:break
            if len(population)<2:break
            k=rng.randint(2,min(4,len(population)))
            combo=tuple(sorted(rng.sample(population,k)))
            if combo not in seen:seen.add(combo);result.append(combo);added+=1
    return result


def run(two_path,three_path,private_path,public_path):
    assert not private_path.resolve().is_relative_to(ROOT)
    start=time.monotonic();deadline=start+900
    data2=two.load(two_path);data3=json.loads(three_path.read_text(encoding='utf-8'))
    m2=two.Model(data2);m3=three.load_model(three_path);three.assert_accepted_baseline(m3)
    assert len(m2.formulas)==16 and len({r['output'] for r in m2.formulas})==10
    counters=collections.Counter();certificates=[];private=[];sample_manifest=[]
    for arity,data,model,pools in [(2,data2,m2,(m2.powders,m2.fluids)),(3,data3,m3,(m3.powders,m3.fluids,m3.essences))]:
        for ti,(label,formula) in enumerate(selection(data['formulas'],model.tags,pools,SEED+arity)):
            target=tuple(formula[k] for k in ('powder','fluid','essence') if k in formula)
            sample_manifest.append(dict(arity=arity,selection=label,output=formula['output'],target=target))
            rng=random.Random(SEED+arity*1000+ti)
            surfaces=set()
            while len(surfaces)<32:
                surfaces.add(tuple(tuple(sorted((t,)+tuple(rng.sample([x for x in pool if x!=t],2)))) for t,pool in zip(target,pools)))
            # Freeze fields and stable priors before evaluating clue packages.
            fields=[]
            for surface in sorted(surfaces):
                tuples=tuple(itertools.product(*surface))
                if arity==3:
                    stable=sorted({e for t in tuples for e in edges(t) if reasoning.stable_relation(m3,e)})
                    other=[e for e in stable if e not in edges(target)]
                    anchor=tuple(rng.sample(other,1)) if other else ()
                    fields.append((surface,tuples,(anchor,anchor+(edges(target)[ti%2],))))
                else:fields.append((surface,tuples,((),)))
            options=[];evaluated=valid=0
            for fi,(surface,tuples,prior_variants) in enumerate(fields):
                if time.monotonic()>deadline:break
                counters['fields']+=1;full=(1<<len(tuples))-1;targetbit=1<<tuples.index(target)
                if arity==2:
                    rawclues=two.target_clues(m2,target,'composite');clues=[]
                    for spec in rawclues:
                        mask=sum(1<<i for i,t in enumerate(tuples) if two.eval_clue(m2,spec,t))
                        if max(2,math.ceil(len(tuples)/2))<=mask.bit_count()<len(tuples):
                            clues.append((spec[0],spec,mask))
                    compatible=full
                else:
                    rawclues,_,_=reasoning.generate_true_weak_clues(m3,m3.tags,target,surface)
                    clues=[(c[0],c[2],c[3]) for c in rawclues]
                    compatible=sum(1<<i for i,t in enumerate(tuples) if all(reasoning.stable_relation(m3,e) for e in edges(t)))
                for combo in package_samples(clues,rng):
                    evaluated+=1;counters['packages']+=1
                    masks=[clues[i][2] for i in combo];live=intersects(masks,full)
                    answer=live if arity==2 else live&compatible
                    if answer!=targetbit:counters['rejectAnswerSet']+=1;continue
                    omissions=[(intersects([m for j,m in enumerate(masks) if j!=drop],full)&compatible).bit_count()
                               for drop in range(len(masks))]
                    if any(n<=1 for n in omissions):counters['rejectFullModelRedundancy']+=1;continue
                    valid+=1;counters['valid']+=1
                    report=summarize_package(clues,combo,tuples,model.tags)
                    report.update(tagCompatible=live.bit_count(),omissionAnswerCounts=omissions,
                                  fieldPropertyHistogram=dict(collections.Counter(len(model.tags[x]) for pool in surface for x in pool)))
                    if arity==3 and not any(e in edges(t) for e in prior_variants[0]
                                           for i,t in enumerate(tuples) if live>>i&1):
                        counters['unrelatedPriorConfigurations']+=1
                        continue
                    options.append(dict(field=fi,surface=surface,tuples=tuples,priors=prior_variants,clues=[clues[i] for i in combo],
                                        live=live,report=report))
            # Find a matched field first; do not imply unmatched causal contrasts.
            grouped=collections.defaultdict(list)
            for o in options:grouped[o['field']].append(o)
            matched=[rows for rows in grouped.values() if any(o['report']['controlProxy'] for o in rows)
                     and any(not o['report']['controlProxy'] for o in rows)]
            rows=max(matched,key=len) if matched else (max(grouped.values(),key=len) if grouped else [])
            keep=[]
            controls=[o for o in rows if o['report']['controlProxy']]
            richer=[o for o in rows if not o['report']['controlProxy']]
            if controls:keep.append(min(controls,key=lambda o:o['report']['crossSlotClauses']))
            if richer:keep.append(max(richer,key=lambda o:(o['report']['derivedAntecedents'],o['report']['crossSlotClauses'])))
            if rows:
                remaining=[o for o in rows if o not in keep]
                if remaining:keep.append(max(remaining,key=lambda o:len(set(o['report']['families']))))
            target_report=dict(arity=arity,selection=label,evaluated=evaluated,valid=valid,
                               matchedContrast=bool(matched),retained=len(keep),certificates=[])
            for ki,o in enumerate(keep):
                rep=dict(o['report']);rep['routes']=[]
                if arity==3:
                    for pi,priors in enumerate(o['priors']):
                        taglive=[t for i,t in enumerate(o['tuples']) if o['live']>>i&1]
                        relevant=bool(priors) and any(e in edges(t) for e in priors for t in taglive)
                        entry=dict(answerEdgePriors=sum(e in edges(target) for e in priors),stablePriors=len(priors),anchorRelevant=relevant,
                                   threeSubmissionFraction=min(3,len(taglive))/len(taglive),policyRoutes=[])
                        for variant in range(3):
                            rr=route(o['tuples'],o['live'],priors,lambda e:reasoning.stable_relation(m3,e),SEED+variant)
                            assert rr['success']
                            rr.update(slack6=6-rr['tests'],slack9=9-rr['tests'])
                            private.append(dict(arity=arity,target=target,package=ki,prior=pi,route=rr))
                            entry['policyRoutes'].append({k:v for k,v in rr.items() if k!='history'})
                        rep['routes'].append(entry)
                else:rep['publicDeductionCandidates']=1
                target_report['certificates'].append(rep)
                private.append(dict(arity=arity,target=target,field=o['surface'],priors=o['priors'],clues=o['clues']))
            certificates.append(target_report)
    source_files=[Path(__file__),Path(two.__file__),Path(three.__file__),Path(reasoning.__file__)]
    result=dict(seed=SEED,scope='six structurally selected variants; bounded diagnostic, not corpus coverage',
                sourceHashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in source_files},
                inputHashes={str(i):hashlib.sha256(p.read_bytes()).hexdigest() for i,p in enumerate((two_path,three_path),2)},
                counters=dict(counters),timedOut=time.monotonic()>deadline,seconds=round(time.monotonic()-start,3),
                selected=certificates,limits=dict(targets=6,fields=192,packages=49152,certificates=18,seconds=900))
    private_path.parent.mkdir(parents=True,exist_ok=True)
    private_path.write_text(json.dumps(dict(sample=sample_manifest,certificates=private),indent=2),encoding='utf-8')
    public_path.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(dict(counters=result['counters'],retained=sum(x['retained'] for x in certificates),seconds=result['seconds'],timedOut=result['timedOut']),indent=2))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('two',type=Path);p.add_argument('three',type=Path)
    p.add_argument('private_certificates',type=Path);p.add_argument('aggregate_report',type=Path)
    a=p.parse_args();run(a.two,a.three,a.private_certificates,a.aggregate_report)
