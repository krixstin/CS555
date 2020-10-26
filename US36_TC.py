# US30 Test Cases: List living married
# Author: Kristin Kim
"""
This is set for 23 DEC 2014
"""

from US36 import recent_death
import unittest


class TestRecentMarriage(unittest.TestCase):

    def setUp(self):
        pass

    def test_recent(self):
        self.assertTrue(recent_death("3 DEC 2014"))
        self.assertTrue(recent_death("Gabriela Geronimo"))

    def test_not_recent(self):
        self.assertFalse(recent_death("Javier Diaz"))
        self.assertFalse(recent_death("Maria Santos"))
        self.assertFalse(recent_death("Cesar Diaz"))
        self.assertFalse(recent_death("19 JAN 1978"))


if __name__ == "__main__":
    unittest.main()

