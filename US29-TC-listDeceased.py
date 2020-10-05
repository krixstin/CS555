# US29 Test Cases: List Deceased
# Author: Kristin Kim

import US29-listDeceased.py
import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        pass

    def T_deceased(self):
        self.assertTrue(listDeceased("Federico Diaz"))
        self.assertTrue(listDeceased("Maria Santos"))
        self.assertTrue(listDeceased("Gabriela Geronimo"))

    def F_deceased(self):
        self.assertFalse(listDeceased("Ana Castro"))
        self.assertFalse(listDeceased("Federico Dias"))
        self.assertFalse(listDeceased("Daisy Guerrero"))
        self.assertFalse(listDeceased("Cesar Jr Geronimo"))


if __name__ == "__main__":
    unittest.main()
