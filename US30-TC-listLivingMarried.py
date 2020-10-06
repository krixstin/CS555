# US30 Test Cases: List living married
# Author: Kristin Kim

import US30-listLivingMarried.py
import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        pass

    def T_livingMarried(self):
        self.assertTrue(livingMarried("Ana Castro"))
        self.assertTrue(livingMarried("Federico Dias"))
        self.assertTrue(livingMarried("Daisy Guerrero"))
        self.assertTrue(livingMarried("Cesar Jr Geronimo"))
        self.assertTrue(livingMarried("Elena Cruz"))
        self.assertTrue(livingMarried("Carlos Alayon"))

    def notMarried(self):
        self.assertFalse(livingMarried("Javier Diaz"))
        self.assertFalse(livingMarried("Xavier Diaz"))
        self.assertFalse(livingMarried("Daileen Pena"))
        self.assertFalse(livingMarried("Derek Pena"))
        self.assertFalse(livingMarried("Dariel Pena"))
        self.assertFalse(livingMarried("Miguel Adonis Diaz"))

    def deceased(self):
        self.assertFalse(livingMarried("Federico Diaz"))
        self.assertFalse(livingMarried("Maria Santos"))
        self.assertFalse(livingMarried("Gabriela Geronimo"))


if __name__ == "__main__":
    unittest.main()
