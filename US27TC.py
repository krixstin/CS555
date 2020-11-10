# US27 Test Cases: Individual age
# Author: Kristin Kim

from US27 import individual_age
import unittest


class TestLivingMarried(unittest.TestCase):

    def setUp(self):
        pass

    def test_correct(self):
        self.assertTrue(individual_age(('Javier Diaz', 20)))
        self.assertTrue(individual_age(('Katy Severino', 12)))

    def test_incorrect(self):
        self.assertFalse(individual_age(("Javier Diaz", 40)))
        self.assertFalse(individual_age(('Emil Alayon', 20)))


if __name__ == "__main__":
    unittest.main()
