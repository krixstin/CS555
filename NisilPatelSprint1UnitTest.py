import unittest

import UniqueChecker


class TestStringMethods(unittest.TestCase):

    def test_unique(self):
        self.assertTrue(UniqueChecker.uniqueID(['@I1@','@I3@','@I4@','@I5@','@I2@']))

    def test_1_item(self):
        self.assertTrue(UniqueChecker.uniqueID(['@I2@']))

    def test_no_item(self):
        self.assertTrue(UniqueChecker.uniqueID([]))

    def test_duplicate(self):
        self.assertFalse(UniqueChecker.uniqueID(['@I1@', '@I3@', '@I1@', '@I5@', '@I2@']))

    def test_multi_duplicate(self):
        self.assertFalse(UniqueChecker.uniqueID(['@I1@', '@I3@', '@I1@', '@I5@', '@I3@']))


if __name__ == '__main__':
    unittest.main()
