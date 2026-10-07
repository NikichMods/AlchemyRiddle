"""One frozen private package; public-state policies and aggregate Science costs."""
import argparse
import collections
import functools
import hashlib
import itertools
import json
import random
import time
from pathlib import Path

import bounded_quality_diagnostic as bounded
import progression_variable_field_screen as three
import reasoning_diversity_screen as reasoning

ROOT = Path(__file__).resolve().parents[2]
SEED = 20261007


class Investigation:
    def __init__(self, triples, priors, oracle, policy, deadline=None, stop_unique=False):
        self.triples = tuple(triples)
        self.priors = dict.fromkeys(priors, True)
        self.oracle = oracle
        self.policy = policy
        self.stop_unique = stop_unique
        self.deadline = deadline or time.monotonic() + 300
        self.edges = sorted({e for t in triples for e in bounded.edges(t)} - set(priors))
        self.index = {e: i for i, e in enumerate(self.edges)}
        self.outcomes = {}
        self.states = 0
        self._visit = None

    def known(self, tested):
        result = dict(self.priors)
        result.update({e: self.outcomes[i] for i, e in enumerate(self.edges) if tested >> i & 1})
        return result

    def public_choices(self, tested, active):
        """This method never reads outcomes of unqueried edges or the target."""
        known = self.known(tested)
        survivors = [i for i, t in enumerate(self.triples)
                     if all(known.get(e) is not False for e in bounded.edges(t))]
        if any(all(known.get(e) is True for e in bounded.edges(self.triples[i]))
               for i in survivors):
            return 'success', (), survivors
        if not survivors:
            return 'failure', (), survivors
        if self.stop_unique and len(survivors) == 1:
            return 'deduced', (), survivors
        unknown = sorted({e for i in survivors for e in bounded.edges(self.triples[i]) if e not in known})
        if self.policy == 'balanced':
            scores = {}
            for e in unknown:
                affected = [i for i in survivors if e in bounded.edges(self.triples[i])]
                support = sum(any(known.get(x) is True for x in bounded.edges(self.triples[i]))
                              for i in affected)
                scores[e] = (min(len(affected), len(survivors) - len(affected)), support)
            best = max(scores.values())
            return 'query', tuple((self.index[e], -1) for e in unknown if scores[e] == best), survivors
        if active not in survivors:
            support = {i: sum(known.get(e) is True for e in bounded.edges(self.triples[i])) for i in survivors}
            best = max(support.values())
            return 'candidate', tuple((-1, i) for i in survivors if support[i] == best), survivors
        missing = [e for e in bounded.edges(self.triples[active]) if e not in known]
        sharing = {e: sum(e in bounded.edges(self.triples[i]) for i in survivors) for e in missing}
        best = max(sharing.values())
        return 'query', tuple((self.index[e], active) for e in sorted(missing) if sharing[e] == best), survivors

    def observe(self, edge_index):
        if edge_index not in self.outcomes:
            self.outcomes[edge_index] = bool(self.oracle(self.edges[edge_index]))

    def distribution(self, tested=0, active=-1):
        @functools.lru_cache(None)
        def visit(tested, active):
            self.states += 1
            if self.states > 200000 or time.monotonic() > self.deadline:
                raise RuntimeError('predeclared state/time cap exceeded')
            kind, choices, _ = self.public_choices(tested, active)
            if kind in ('success', 'deduced'):
                return {0: 1.0}
            if kind == 'failure':
                raise AssertionError('fixed unique answer was lost')
            result = collections.defaultdict(float)
            for edge, candidate in choices:
                if kind == 'query':
                    self.observe(edge)
                    child = visit(tested | (1 << edge), candidate)
                    shift = 1
                else:
                    child = visit(tested, candidate)
                    shift = 0
                for count, weight in child.items():
                    result[count + shift] += weight / len(choices)
            return dict(result)
        if self._visit is None:
            self._visit = visit
        hist = self._visit(tested, active)
        assert abs(sum(hist.values()) - 1) < 1e-9
        mean = sum(n * weight for n, weight in hist.items())
        return dict(pairTests=dict(sorted(hist.items())), min=min(hist), max=max(hist),
                    uniformTieMean=mean, within3=sum(w for n, w in hist.items() if n <= 3),
                    within5=sum(w for n, w in hist.items() if n <= 5),
                    scienceRange=[2 * min(hist) + 5, 2 * max(hist) + 5],
                    uniformTieMeanScience=2 * mean + 5, memoizedStates=self.states)

    def replay(self, seed):
        rng = random.Random(seed)
        tested, active = 0, -1
        history = []
        while True:
            kind, choices, survivors = self.public_choices(tested, active)
            if kind in ('success', 'deduced'):
                return dict(tests=len(history), remaining=len(survivors),
                            science=2 * len(history) + 5, stopReason=kind, history=history)
            assert kind != 'failure'
            edge, active = rng.choice(choices)
            if kind == 'query':
                self.observe(edge)
                tested |= 1 << edge
                history.append(dict(edge=self.edges[edge], stable=self.outcomes[edge],
                                    liveBefore=len(survivors), testedMask=tested, active=active))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(input_path, certificate_path, private_output, public_output):
    start = time.monotonic()
    deadline = start + 300
    assert not private_output.resolve().is_relative_to(ROOT)
    source = json.loads(certificate_path.read_text(encoding='utf-8'))
    manifest = next(s for s in source['sample'] if s['arity'] == 3 and s['selection'] == 'rich')
    target = tuple(manifest['target'])
    packages = [c for c in source['certificates'] if c['arity'] == 3
                and tuple(c['target']) == target and 'field' in c]
    package = packages[1]
    all_triples = tuple(itertools.product(*package['field']))
    live = bounded.intersects([c[2] for c in package['clues']], (1 << len(all_triples)) - 1)
    triples = tuple(t for i, t in enumerate(all_triples) if live >> i & 1)
    priors = tuple(tuple(e) for e in package['priors'][0])
    assert len(triples) == 9 and not any(e in bounded.edges(target) for e in priors)
    model = three.load_model(input_path)
    three.assert_accepted_baseline(model)
    oracle = lambda e: reasoning.stable_relation(model, e)
    assert all(oracle(e) for e in priors)
    answers = [t for t in triples if all(oracle(e) for e in bounded.edges(t))]
    assert answers == [target]
    old = [bounded.route(all_triples, live, priors, oracle, SEED + i)['tests'] for i in range(3)]
    assert old == [3, 11, 11]
    unknown = sorted({e for t in triples for e in bounded.edges(t)} - set(priors))
    sharing = collections.Counter(sum(e in bounded.edges(t) for t in triples) for e in unknown)
    policies = {}
    private = dict(target=target, field=package['field'], clues=package['clues'], priors=priors, policies={})
    for name in ('balanced', 'candidate_first'):
        instance = Investigation(triples, priors, oracle, name, deadline)
        replays = [instance.replay(SEED + i) for i in range(3)]
        if name == 'balanced':
            assert [r['tests'] for r in replays] == old
        policies[name] = instance.distribution()
        policies[name]['seedTests'] = [r['tests'] for r in replays]
        policies[name]['observedRouteCheckpoints'] = []
        for replay in replays:
            checkpoints = []
            for step, h in enumerate(replay['history'], 1):
                kind, _, surviving = instance.public_choices(h['testedMask'], h['active'])
                continuation = instance.distribution(h['testedMask'], h['active'])
                # Certification fixes a valid answer: one final check, no guessing.
                direct_mean = 5 if kind == 'success' else 5 * (len(surviving) + 1) / 2
                checkpoints.append(dict(pairChecksSpent=step, liveTriples=len(surviving),
                                        certified=kind == 'success',
                                        remainingPairPolicyMeanScience=continuation['uniformTieMeanScience'],
                                        remainingDirectOrderingMeanScience=direct_mean))
            policies[name]['observedRouteCheckpoints'].append(checkpoints)
        private['policies'][name] = replays
    finishing = {}
    for name in ('balanced', 'candidate_first'):
        instance = Investigation(triples, priors, oracle, name, deadline, stop_unique=True)
        replays = [instance.replay(SEED + i) for i in range(3)]
        finishing[name] = instance.distribution()
        finishing[name]['seedTests'] = [r['tests'] for r in replays]
        finishing[name]['seedStopReasons'] = [r['stopReason'] for r in replays]
        private['policies'][name + '_singleton_stop'] = replays
    # Exact mean for a uniform permutation of nine hypotheses; no player prior.
    n = len(triples)
    direct = dict(candidates=n, scienceRange=[5, 5 * n],
                  uniformOrderingMeanScience=5 * (n + 1) / 2,
                  distribution={5 * i: 1 / n for i in range(1, n + 1)},
                  twoSubmissionSuccessFraction=2 / n, threeSubmissionSuccessFraction=3 / n)
    result = dict(scope='one fixed rich package, zero initial answer-edge support',
                  complete=True, pairCost=2, tripleCost=5, attemptCap=None,
                  hypotheses=n, unknownRelevantEdges=len(unknown),
                  unknownEdgeSharingHistogram=dict(sorted(sharing.items())),
                  stablePriors=len(priors), hypothesesSupportedByPrior=sum(
                      any(e in bounded.edges(t) for e in priors) for t in triples),
                  policies=policies, singletonStopSensitivity=finishing, directSubmissions=direct,
                  sourceHashes={p.name: sha(p) for p in (Path(__file__), Path(bounded.__file__),
                                                        Path(three.__file__), Path(reasoning.__file__))},
                  inputHashes=dict(corpus=sha(input_path), certificates=sha(certificate_path)),
                  seconds=round(time.monotonic() - start, 3),
                  limits=dict(packages=1, statesPerPolicy=200000, seconds=300),
                  caveat='Uniform policy ties/orderings are mechanical baselines, not human probabilities.')
    private_output.write_text(json.dumps(private, indent=2), encoding='utf-8')
    public_output.write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('corpus', 'certificates', 'private_output', 'public_output'):
        parser.add_argument(name, type=Path)
    args = parser.parse_args()
    run(args.corpus, args.certificates, args.private_output, args.public_output)
