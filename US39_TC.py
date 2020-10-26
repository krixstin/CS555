# US30 Test Cases: List living married
# Author: Kristin Kim
"""
This is set for 10 APR
"""

from US39 import recent_marriage
import unittest


class TestRecentMarriage(unittest.TestCase):

    def setUp(self):
        pass

    def test_recent(self):
        self.assertTrue(recent_marriage("28 APR 1970"))
        self.assertTrue(recent_marriage("Daisy Guerrero"))
        self.assertTrue(recent_marriage("9 MAY 2010"))
        self.assertTrue(recent_marriage("Stephanie Gonzalez"))

    def test_not_recent(self):
        self.assertFalse(recent_marriage("Javier Diaz"))
        self.assertFalse(recent_marriage("4 MAY 1978"))
        self.assertFalse(recent_marriage("Cesar Diaz"))
        self.assertFalse(recent_marriage("19 JAN 1978"))


if __name__ == "__main__":
    unittest.main()

