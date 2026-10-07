"""Regression checks for unchanged baseline and additive pacing preferences."""
import collections
import statistics
import unittest
import generator_route_ranking as ranking
import reasoning_diversity_screen as reasoning


def row(family, relation, mean):
    return dict(families=(family,), semantics=((family, 'synthetic'),), relation_mode=relation,
                route=[dict(mean=mean, observedStablePriors=0)])


class Ranking(unittest.TestCase):
    def test_baseline_reproduces_existing_sequence_metrics(self):
        options = [[row('xor', 'PF', 3), row('count', 'FE', 5), row('imp_pos_fwd', 'mixed', 7)]
                   for _ in range(8)]
        order = list(range(8))
        expected = reasoning.anti_clump_sequence(options, order, 19)
        records = ranking.select_sequence(options, order, 19, 0, 3, 0)
        chosen = [options[r['target']][r['index']] for r in records]
        self.assertEqual(expected['family_counts'], dict(collections.Counter(
            f for r in chosen for f in reasoning.option_family_set(r))))
        self.assertEqual(expected['relation_counts'], dict(collections.Counter(r['relation_mode'] for r in chosen)))
        overlap = statistics.mean(reasoning.jaccard(reasoning.option_family_set(a), reasoning.option_family_set(b))
                                  for a, b in zip(chosen, chosen[1:]))
        self.assertEqual(expected['mean_adjacent_family_overlap'], overlap)

    def test_two_checks_and_earned_shortcuts_are_not_forced_longer(self):
        self.assertEqual(ranking.length_penalty(2, 3), 0)
        self.assertEqual(ranking.length_penalty(0, 3, earned=True), 0)
        self.assertGreater(ranking.length_penalty(1, 3), 0)

    def test_long_routes_get_progressive_penalty(self):
        self.assertEqual(ranking.length_penalty(5, 5), 0)
        self.assertGreater(ranking.length_penalty(8, 5), ranking.length_penalty(7, 5))
        self.assertGreater(ranking.length_penalty(7, 5), ranking.length_penalty(6, 5))

    def test_addition_keeps_pool_but_prefers_shorter_tied_candidate(self):
        options = [[row('xor', 'PF', 3), row('xor', 'PF', 9)]]
        records = ranking.select_sequence(options, [0], 0, 0.5, 3, 0)
        self.assertEqual(records[0]['index'], 0)
        self.assertEqual(len(options[0]), 2)


if __name__ == '__main__':
    unittest.main()
