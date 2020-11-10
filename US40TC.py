# US40 Test Cases: Include input line numbers
# Author: Kristin Kim

from US40 import line_of_code
import unittest


class TestLOC(unittest.TestCase):

    def setUp(self):
        pass

    def test_line(self):
        self.assertEqual(line_of_code("DiazJGedcomProject1.ged"), 391)


if __name__ == "__main__":
    unittest.main()
