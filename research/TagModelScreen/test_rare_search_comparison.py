import collections
import random
import unittest

from rare_search_comparison import BUDGET, focused_pair, proposals
from reasoning_diversity_screen import rare_package_proposals


class RareSearchTests(unittest.TestCase):
    def test_budget_and_unchanged_tail(self):
        groups = {'literal': [0, 1], 'shared': [2], 'xor': [3, 4]}
        baseline = list(proposals(groups, 5, 123, 0, {'shared'}))
        trial = list(proposals(groups, 5, 123, 64, {'shared'}))
        self.assertEqual(len(trial), BUDGET)
        self.assertEqual(trial[64:], baseline[64:])
        self.assertTrue(all(2 in pair and len(pair) == 2 for pair in trial[:64]))

    def test_unavailable_rare_is_exact_fallback(self):
        groups = {'literal': [0, 1], 'xor': [2, 3]}
        self.assertEqual(list(proposals(groups, 5, 123, 0, {'shared'})),
                         list(proposals(groups, 5, 123, 128, {'shared'})))

    def test_multiple_rare_families_receive_attention(self):
        groups = {'rareA': [0], 'rareB': [1], 'ordinary': [2, 3, 4]}
        rng = random.Random(41)
        counts = collections.Counter(i for _ in range(200)
                                     for i in focused_pair(groups, {'rareA', 'rareB', 'absent'}, rng))
        self.assertGreater(counts[0], 50)
        self.assertGreater(counts[1], 50)

    def test_invalid_budget(self):
        with self.assertRaises(ValueError):
            list(proposals({'literal': [0, 1]}, 5, 1, BUDGET + 1, set()))

    def test_adopted_default_and_tiny_budget(self):
        groups = {'literal': [0, 1], 'shared': [2], 'xor': [3, 4]}
        self.assertEqual(list(rare_package_proposals(groups, 5, 123)),
                         list(proposals(groups, 5, 123, 64, {'shared'})))
        self.assertEqual(len(list(rare_package_proposals(groups, None, 123,
                                                       reserve=1, budget=1))), 1)

    def test_insufficient_predicates_and_floor(self):
        self.assertEqual(list(proposals({'literal': [0]}, 5, 123, 0, set())), [None]*BUDGET)
        pairs = list(proposals({'literal': [0, 1, 2]}, 3, 123, 0, set()))
        self.assertTrue(all(pair is None or len(pair) == 2 for pair in pairs))


if __name__ == '__main__':
    unittest.main()
