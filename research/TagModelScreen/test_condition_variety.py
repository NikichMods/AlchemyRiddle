"""Synthetic exhaustive truth tables and research-to-Lab integration checks."""
import itertools
from types import SimpleNamespace
import unittest

import bounded_quality_diagnostic as quality
import generator_route_ranking as ranking
import intra_package_review as review
import prepare_corpus_contrast as preparation
import reasoning_diversity_screen as reasoning


def synthetic_field():
    surface = (('p1', 'p2', 'p3'), ('f1', 'f2', 'f3'), ('e1', 'e2', 'e3'))
    tags = dict(p1={'Water', 'Animal'}, p2={'Water', 'Dark'}, p3={'Dark'},
                f1={'Water', 'Animal'}, f2={'Water', 'Dark'}, f3={'Dark'},
                e1={'Water', 'Animal'}, e2={'Water', 'Dark'}, e3={'Dark'})
    model = SimpleNamespace(vocabulary=('Water', 'Animal', 'Dark'), tags=tags)
    return model, surface


class ConditionVariety(unittest.TestCase):
    def test_new_masks_match_independent_truth_tables_for_every_target(self):
        model, surface = synthetic_field()
        found = set()
        for target in itertools.product(*surface):
            clues, triples, target_index = reasoning.generate_true_weak_clues(
                model, model.tags, target, surface)
            for family, semantic, spec, mask in clues:
                if family not in ('shared', 'count_mixed'):
                    continue
                found.add(family)
                if family == 'shared':
                    expected = [any(all(tag in model.tags[item] for item in triple)
                                    for tag in model.vocabulary) for triple in triples]
                else:
                    self.assertEqual(len(spec[1]), 3)
                    self.assertGreater(len(set(spec[1])), 1)
                    expected = [sum(spec[1][i] in model.tags[triple[i]] for i in range(3))
                                == spec[2] for triple in triples]
                self.assertEqual(mask, sum(1 << i for i, yes in enumerate(expected) if yes))
                self.assertTrue(expected[target_index])
                self.assertTrue(12 <= sum(expected) <= 26)
                self.assertEqual([review.holds(spec, t, model.tags) for t in triples], expected)
                self.assertEqual(preparation.convert(spec)['kind'],
                                 'sharedTag' if family == 'shared' else 'exactly')
        self.assertEqual(found, {'shared', 'count_mixed'})

    def test_shared_can_use_different_common_properties_and_reject_empty_intersection(self):
        model, _ = synthetic_field()
        self.assertTrue(review.holds(('shared',), ('p1', 'f1', 'e1'), model.tags))
        self.assertTrue(review.holds(('shared',), ('p3', 'f3', 'e3'), model.tags))
        self.assertFalse(review.holds(('shared',), ('p1', 'f3', 'e1'), model.tags))

    def test_flat_mixed_counts_keep_existing_control_rejection(self):
        model, surface = synthetic_field()
        clues, triples, _ = reasoning.generate_true_weak_clues(
            model, model.tags, ('p1', 'f1', 'e1'), surface)
        converted = [(c[0], c[2], c[3]) for c in clues if c[0] == 'count_mixed']
        self.assertGreater(len(converted), 1)
        result = quality.summarize_package(converted, (0, 1), triples, model.tags)
        self.assertTrue(result['controlProxy'])

    def test_each_new_family_can_pass_the_unchanged_package_gates(self):
        model, surface = synthetic_field()
        raw, triples, target_index = reasoning.generate_true_weak_clues(
            model, model.tags, ('p1', 'f1', 'e1'), surface)
        cases = [
            ({('p1', 'f1'), ('p2', 'f2'), ('p3', 'f3')},
             {('f1', 'e1'), ('f1', 'e3'), ('f2', 'e2'), ('f2', 'e3'),
              ('f3', 'e1'), ('f3', 'e3')},
             (('count_mixed', ('Water', 'Animal', 'Dark'), 2),
              ('xor', 0, 'Dark', 1, 'Water'))),
            ({(p, f) for p in ('p1', 'p3') for f in surface[1]},
             {('f1', 'e1'), ('f2', 'e1')},
             (('shared',), ('xor', 1, 'Dark', 2, 'Water'))),
        ]
        for pf, fe, specs in cases:
            model.stable_pf, model.stable_fe = pf, fe
            combo = tuple(next(i for i, c in enumerate(raw) if c[2] == spec)
                          for spec in specs)
            full = (1 << len(triples)) - 1
            compatible = sum(1 << i for i, t in enumerate(triples)
                             if all(reasoning.stable_relation(model, e) for e in quality.edges(t)))
            masks = [raw[i][3] for i in combo]
            self.assertEqual(quality.intersects(masks, full) & compatible, 1 << target_index)
            self.assertTrue(all((mask & compatible).bit_count() > 1 for mask in masks))
            self.assertIsNotNone(reasoning.option_from_combo(model, raw, combo, triples, target_index))
            structure = quality.summarize_package([(c[0], c[2], c[3]) for c in raw],
                                                  combo, triples, model.tags)
            self.assertFalse(structure['controlProxy'])
            self.assertEqual(structure['immediatelyHandedAntecedents'], 0)

    def test_new_families_receive_existing_soft_recency_preference(self):
        for family in ('shared', 'count_mixed'):
            row = dict(families=(family,), semantics=((family, 'synthetic'),),
                       relation_mode='PF')
            self.assertGreater(ranking.baseline_score(row, [row], 0),
                               ranking.baseline_score(row, [], 0))

    def test_enumeration_is_deterministic_and_serialized_specs_replay(self):
        import json
        model, surface = synthetic_field()
        args = (model, model.tags, ('p1', 'f1', 'e1'), surface)
        first = reasoning.generate_true_weak_clues(*args)
        self.assertEqual(first, reasoning.generate_true_weak_clues(*args))
        for family, _, spec, mask in first[0]:
            if family in ('shared', 'count_mixed'):
                replay = json.loads(json.dumps(spec))
                self.assertEqual(mask, sum(1 << i for i, t in enumerate(first[1])
                                           if review.holds(replay, t, model.tags)))


if __name__ == '__main__':
    unittest.main()
