"""Focused epistemic checks for the offline route policy; synthetic tuples only."""
import unittest
import bounded_quality_diagnostic as screen


class RouteBoundary(unittest.TestCase):
    def test_first_choice_does_not_depend_on_hidden_outcome(self):
        triples=(('p1','f1','e1'),('p2','f2','e2'))
        first=[]
        class StopAfterQuery(Exception): pass
        for secret in (True,False):
            def oracle(edge):
                first.append((edge,secret))
                raise StopAfterQuery
            with self.assertRaises(StopAfterQuery):
                screen.route(triples,3,(),oracle,20261007)
        self.assertEqual(first[0][0],first[1][0])

    def test_certification_need_not_exhaust_other_hypotheses(self):
        triples=(('p1','f1','e1'),('p2','f2','e2'))
        priors=(('PF','p1','f1'),)
        calls=[]
        def oracle(edge):
            calls.append(edge)
            return True
        result=screen.route(triples,3,priors,oracle,20261007)
        self.assertTrue(result['success'])
        self.assertEqual(result['tests'],1)
        self.assertEqual(result['remaining'],2)
        self.assertEqual(calls,[('FE','f1','e1')])

    def test_negative_edge_is_not_bought_twice(self):
        triples=(('p1','f1','e1'),('p1','f1','e2'),('p2','f2','e3'))
        target_edges=set(screen.edges(triples[2]))
        calls=[]
        def oracle(edge):
            calls.append(edge)
            return edge in target_edges
        result=screen.route(triples,7,(),oracle,20261007)
        self.assertTrue(result['success'])
        self.assertEqual(len(calls),len(set(calls)))
        self.assertGreater(result['negativeTests'],0)
        self.assertEqual(result['certified'],1)


if __name__=='__main__': unittest.main()
