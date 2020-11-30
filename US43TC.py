# US43 Test Cases: List all living Generation Z
# Author: Kristin Kim

from US43 import gen_z
import unittest


class TestRecentMarriage(unittest.TestCase):

    def setUp(self):
        pass

    def test_recent(self):
        self.assertTrue(gen_z('Javier Diaz'))
        self.assertTrue(gen_z('Karen Severino'))
        self.assertTrue(gen_z('Katy Severino'))
        self.assertTrue(gen_z('Emil Alayon'))

    def test_not_recent(self):
        self.assertFalse(gen_z("Javier Evango"))
        self.assertFalse(gen_z("4 MAY 1978"))
        self.assertFalse(gen_z("Cesar Diaz"))
        self.assertFalse(gen_z("19 JAN 1978"))


if __name__ == "__main__":
    unittest.main()

