# SPDX-License-Identifier: MPL-2.0
import copy
import json
import unittest

from campaign_corpus import build, verify
from campaign_knowledge import Knowledge
from campaign_names import target_names
from science_route_comparison import Investigation
import generator_route_ranking as ranking
from campaign_sequence_screen import freeze_json, resolved_indices


def tiny():
    ingredients = [dict(name='a', type='Powder', tags=['Plant']),
                   dict(name='b', type='Fluid', tags=['Plant', 'Slime']),
                   dict(name='c', type='Essence', tags=['Insect'])]
    two = dict(ingredients=ingredients, formulas=[dict(output='x', powder='a', fluid='b')])
    three = dict(ingredients=ingredients, formulas=[dict(output='y', powder='a', fluid='b', essence='c')])
    return {'ordinary-2': two, 'core-2': copy.deepcopy(two), 'ordinary-3': three}


class CampaignFoundation(unittest.TestCase):
    def test_certified_chain_need_not_refute_every_other_unobserved_candidate(self):
        triples = (('a', 'b', 'c'), ('x', 'y', 'z'))
        priors = {('PF', 'a', 'b'): True, ('FE', 'b', 'c'): True}
        inv = Investigation(triples, priors, lambda e: self.fail('unneeded experiment'),
                            'balanced', stop_unique=True)
        self.assertEqual(inv.public_choices(0, -1)[2], [0, 1])
        self.assertEqual(resolved_indices(inv, 0, -1), [0])

    def test_saved_nested_semantics_restore_for_unchanged_selector(self):
        semantics = [['count_mixed', [['P', 'Plant'], ['F', 'Water']]], ['shared']]
        row = dict(families=['count_mixed', 'shared'], relation_mode='PF',
                   semantics=freeze_json(semantics))
        self.assertIsInstance(ranking.baseline_score(row, [row], 1), float)

    def test_reordering_source_keeps_identity_and_names(self):
        data = tiny()
        manifest, renamed, mapping = build(data)
        for d in data.values():
            d['ingredients'] = list(reversed(d['ingredients']))
            d['formulas'] = list(reversed(d['formulas']))
        self.assertEqual(manifest, build(data)[0])
        self.assertEqual(mapping, build(data)[2])

    def test_structural_verification_rejects_recipe_and_tag_mutation(self):
        data = tiny()
        manifest, renamed, mapping = build(data)
        changed = copy.deepcopy(renamed)
        changed['ordinary-3']['formulas'][0]['essence'] = mapping['ingredients']['a']
        with self.assertRaisesRegex(ValueError, 'structure'):
            verify(data, changed, mapping, manifest)
        changed = copy.deepcopy(renamed)
        changed['ordinary-3']['ingredients'][0]['tags'].append('Water')
        with self.assertRaisesRegex(ValueError, 'semantics'):
            verify(data, changed, mapping, manifest)

    def test_conflicting_shared_properties_and_missing_bank_fail_closed(self):
        data = tiny()
        data['ordinary-3'] = copy.deepcopy(data['ordinary-3'])
        data['ordinary-3']['ingredients'][0]['tags'] = ['Water']
        with self.assertRaisesRegex(ValueError, 'conflict'):
            build(data)
        data = tiny()
        for d in data.values():
            d['ingredients'][0]['tags'] = ['Imaginary']
        with self.assertRaisesRegex(ValueError, 'signature'):
            build(data)

    def test_target_titles_do_not_depend_on_answer_tags(self):
        before = target_names(['t001', 't002'], 42)
        self.assertEqual(before, target_names(['t002', 't001'], 42))
        with self.assertRaises(TypeError):
            target_names(['t001'], 42, hidden_answer='anything')

    def test_failed_mixture_does_not_create_pair_facts(self):
        knowledge = Knowledge()
        knowledge.observe(('PF', 'a', 'b'), False, 'experiment')
        knowledge.mixture(('a', 'b', 'c'), False, 'failed hypothesis')
        self.assertEqual(knowledge.priors(), {('PF', 'a', 'b'): False})
        self.assertEqual(Knowledge.restore(json.loads(json.dumps(knowledge.snapshot()))).snapshot(),
                         knowledge.snapshot())
        with self.assertRaisesRegex(ValueError, 'Contradictory'):
            knowledge.observe(('PF', 'a', 'b'), True, 'different source')

    def test_success_learns_adjacent_edges_but_two_slot_does_not(self):
        knowledge = Knowledge()
        knowledge.mixture(('a', 'b'), True, 'two')
        self.assertEqual(knowledge.priors(), {})
        knowledge.mixture(('a', 'b', 'c'), True, 'three')
        self.assertEqual(knowledge.priors(), {('PF', 'a', 'b'): True, ('FE', 'b', 'c'): True})

    def test_negative_priors_reject_hypotheses_without_oracle_or_retest(self):
        triples = (('a', 'b', 'c'), ('a', 'b', 'd'), ('x', 'y', 'z'))
        priors = {('PF', 'a', 'b'): False}
        def forbidden(edge):
            self.fail('Known negative observation bought again')
        for policy in ('balanced', 'candidate_first'):
            inv = Investigation(triples, priors, forbidden, policy, stop_unique=True)
            self.assertEqual(inv.replay(1)['tests'], 0)
            self.assertEqual(inv.public_choices(0, -1)[2], [2])
            self.assertEqual(inv.distribution()['pairTests'], {0: 1.0})

    def test_mixed_polarities_survive_restore_and_legacy_routes(self):
        triples = (('a', 'b', 'c'), ('x', 'y', 'z'))
        priors = {('PF', 'a', 'b'): False, ('PF', 'x', 'y'): True}
        inv = Investigation(triples, priors, lambda e: True, 'balanced')
        self.assertEqual(inv.replay(1)['tests'], 1)
        self.assertEqual(inv.priors, priors)
        edge = ('PF', 'x', 'y')
        mapping = Investigation(triples, {edge: True}, lambda e: True, 'balanced')
        legacy = Investigation(triples, [edge], lambda e: True, 'balanced')
        self.assertEqual(mapping.replay(7), legacy.replay(7))
        with self.assertRaisesRegex(ValueError, 'booleans'):
            Investigation(triples, {edge: 'false'}, lambda e: True, 'balanced')

    def test_earned_negative_shortcut_has_no_artificial_minimum_length_cost(self):
        row = dict(families=['count'], relation_mode='PF', semantics=[('count', 'synthetic')],
                   clues=[], route=[dict(mean=0, observedStablePriors=0, observedIncompatiblePriors=1)])
        self.assertEqual(ranking.selection_score(row, [], 0, .25, 3, 0),
                         ranking.baseline_score(row, [], 0))


if __name__ == '__main__':
    unittest.main()
