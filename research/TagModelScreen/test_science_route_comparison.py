"""Synthetic boundary tests for locked-candidate and exhaustive tie accounting."""
import unittest

from science_route_comparison import Investigation


class ScienceRoutes(unittest.TestCase):
    def test_initial_choices_do_not_read_hidden_outcomes(self):
        triples = (('p1', 'f1', 'e1'), ('p2', 'f2', 'e2'))
        def forbidden(edge):
            self.fail('selection inspected unearned chemistry')
        for policy in ('balanced', 'candidate_first'):
            investigator = Investigation(triples, (), forbidden, policy)
            investigator.public_choices(0, -1)
            if policy == 'candidate_first':
                investigator.public_choices(0, 0)

    def test_exact_tie_distribution_on_two_disjoint_candidates(self):
        triples = (('p1', 'f1', 'e1'), ('p2', 'f2', 'e2'))
        for policy in ('balanced', 'candidate_first'):
            investigator = Investigation(triples, (), lambda e: 'f1' in e, policy)
            result = investigator.distribution()
            # True candidate first: two tests; false first: one negative + two.
            self.assertEqual(result['pairTests'], {2: 0.5, 3: 0.5})
            self.assertEqual(result['uniformTieMeanScience'], 10)

    def test_candidate_is_kept_until_refuted(self):
        triples = (('p1', 'f1', 'e1'), ('p2', 'f2', 'e2'))
        investigator = Investigation(triples, (), lambda e: True, 'candidate_first')
        kind, choices, _ = investigator.public_choices(0, 0)
        edge, candidate = choices[0]
        investigator.observe(edge)
        kind, choices, _ = investigator.public_choices(1 << edge, candidate)
        self.assertEqual(kind, 'query')
        self.assertTrue(all(c == 0 for _, c in choices))
        self.assertTrue(all('f1' in investigator.edges[e] for e, _ in choices))

    def test_failed_candidate_reuses_known_negative(self):
        triples = (('p1', 'f1', 'e1'), ('p1', 'f1', 'e2'), ('p2', 'f2', 'e3'))
        calls = []
        def oracle(e):
            calls.append(e)
            return 'f2' in e
        investigator = Investigation(triples, (), oracle, 'candidate_first')
        result = investigator.replay(20261007)
        self.assertEqual(len(calls), len(set(calls)))
        self.assertEqual(result['remaining'], 1)
        self.assertEqual(result['science'], 2 * result['tests'] + 5)

    def test_singleton_deduction_does_not_buy_ceremonial_edges(self):
        triples = (('p1', 'f1', 'e1'), ('p2', 'f2', 'e2'))
        calls = []
        def oracle(e):
            calls.append(e)
            return False
        investigator = Investigation(triples, (), oracle, 'candidate_first', stop_unique=True)
        edge = investigator.index[('PF', 'p1', 'f1')]
        investigator.observe(edge)
        kind, choices, survivors = investigator.public_choices(1 << edge, 0)
        self.assertEqual(kind, 'deduced')
        self.assertEqual(survivors, [1])
        self.assertEqual(choices, ())
        result = investigator.distribution(1 << edge, 0)
        self.assertEqual(result['pairTests'], {0: 1})
        self.assertEqual(result['uniformTieMeanScience'], 5)
        self.assertEqual(len(calls), 1)


if __name__ == '__main__':
    unittest.main()
