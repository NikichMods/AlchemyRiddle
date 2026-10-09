"""Family-first draws must remove multiplicity bias without forbidding repetitions."""
import random
import unittest
from reasoning_diversity_screen import family_groups, draw_family_first


class FamilyFirst(unittest.TestCase):
    def test_family_size_does_not_determine_first_draw_probability(self):
        groups = family_groups([('shared',)] + [('count_mixed',)] * 100)
        rng = random.Random(20261009)
        rare = sum(draw_family_first(groups, 1, rng) == (0,) for _ in range(2000))
        self.assertTrue(900 < rare < 1100)

    def test_repetition_is_allowed_but_identical_predicate_is_not_reused(self):
        self.assertEqual(draw_family_first({'xor': [0, 1, 2]}, 3, random.Random(4)), (0, 1, 2))

    def test_direction_variants_share_one_root_family(self):
        self.assertEqual(family_groups([('imp_pos_fwd',), ('imp_pos_rev',), ('shared',)]),
                         {'imp_pos': [0, 1], 'shared': [2]})

    def test_insufficient_pool_fails_and_seed_is_reproducible(self):
        groups = {'count': [0], 'xor': [1, 2]}
        self.assertEqual(draw_family_first(groups, 3, random.Random(8)),
                         draw_family_first(groups, 3, random.Random(8)))
        with self.assertRaises(ValueError):
            draw_family_first(groups, 4, random.Random(8))


if __name__ == '__main__':
    unittest.main()
