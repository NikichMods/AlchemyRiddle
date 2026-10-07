"""Check the floor against complete small Boolean clue models, not game recipes."""
import itertools
import unittest
from field_feasibility import supports_necessary_clues


class FieldFloor(unittest.TestCase):
    def test_no_valid_small_model_is_rejected(self):
        # A row states which clues a chemically compatible alternative satisfies.
        for clues in (2, 3):
            target = (True,) * clues
            alternatives = [r for r in itertools.product((False, True), repeat=clues) if r != target]
            for size in range(len(alternatives) + 1):
                for others in itertools.combinations(alternatives, size):
                    necessary = all(any(all(r[j] for j in range(clues) if j != drop)
                                        for r in others) for drop in range(clues))
                    if necessary:
                        self.assertTrue(supports_necessary_clues(size + 1, clues))

    def test_floor_is_attainable(self):
        self.assertFalse(supports_necessary_clues(2, 2))
        self.assertTrue(supports_necessary_clues(3, 2))
        self.assertFalse(supports_necessary_clues(3, 3))
        self.assertTrue(supports_necessary_clues(4, 3))


if __name__ == '__main__':
    unittest.main()
