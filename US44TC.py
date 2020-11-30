# US44 Test Cases: List all living couples nniversaries occured in the last 30 days
# Author: Kristin Kim
"""
This is set for 10 MAY
"""

from US44 import recent_past_marriage
import unittest


class TestPastMarriage(unittest.TestCase):

    def setUp(self):
        pass

    def test_recent_past(self):
        self.assertTrue(recent_past_marriage("28 APR 1970"))
        self.assertTrue(recent_past_marriage("Daisy Guerrero"))
        self.assertTrue(recent_past_marriage("9 MAY 2010"))
        self.assertTrue(recent_past_marriage("Stephanie Gonzalez"))

    def test_not_recent_past(self):
        self.assertFalse(recent_past_marriage("Javier Diaz"))
        self.assertFalse(recent_past_marriage("4 MAY 1978"))
        self.assertFalse(recent_past_marriage("Cesar Diaz"))
        self.assertFalse(recent_past_marriage("19 JAN 1978"))


if __name__ == "__main__":
    unittest.main()

