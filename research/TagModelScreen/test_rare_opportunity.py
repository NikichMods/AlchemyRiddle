"""Boundaries of rarity preference: bounded, exposure-aware, no forced outcome."""
import unittest
from rare_opportunity_screen import opportunity_prior, opportunity_bonus, select, restore_pool_semantics


def row(family, mean=3):
    return dict(families=(family,), semantics=((family, 'synthetic'),), relation_mode='PF',
                route=[dict(mean=mean, observedStablePriors=0)])


class RareOpportunity(unittest.TestCase):
    def test_nested_semantic_keys_replay_after_json_round_trip(self):
        import json
        candidate = row('count_mixed')
        candidate['semantics'] = (('count_mixed', ('Water', 'Dark', 'Animal'), 2),)
        pool = [[candidate], [row('xor')]]
        expected = select(pool, [0, 1], 4, 3, 0, {}, 0)
        recovered = json.loads(json.dumps(pool))
        restore_pool_semantics(recovered)
        self.assertEqual(expected, select(recovered, [0, 1], 4, 3, 0, {}, 0))

    def test_prior_counts_targets_not_repeated_package_instances(self):
        witness = dict(arm='family_first', target=0, families=('shared',))
        a = opportunity_prior([dict(witnesses=[witness])], 20)
        b = opportunity_prior([dict(witnesses=[witness] * 100)], 20)
        self.assertEqual(a, b)
        self.assertEqual(a[0]['shared'], .8)

    def test_recent_exposure_disables_bonus_and_old_exposure_does_not(self):
        prior = {'shared': 1}
        rare, common = row('shared'), row('xor')
        self.assertEqual(opportunity_bonus(rare, [rare, common], prior, .5), 0)
        self.assertEqual(opportunity_bonus(rare, [rare, common, common], prior, .5), .5)

    def test_multiple_rare_families_do_not_stack_bonus(self):
        candidate = dict(families=('shared', 'count_mixed'))
        self.assertEqual(opportunity_bonus(candidate, [], {'shared': .5, 'count_mixed': .8}, 1), .8)

    def test_bonus_does_not_force_poor_route_and_only_candidate_still_works(self):
        rare, common = row('shared', 9), row('xor', 3)
        result = select([[rare, common]], [0], 1, 3, 0, {'shared': 1}, .5)
        self.assertEqual(result[0]['index'], 1)
        self.assertEqual(select([[rare]], [0], 1, 3, 0, {'shared': 1}, .5)[0]['index'], 0)


if __name__ == '__main__':
    unittest.main()
