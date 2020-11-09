import unittest
import US41

# Less than 150 years old
class TestStringMethods(unittest.TestCase):
    
    #Get the ouput from the Tables.txt file
    def test_all_match(self):
        self.assertTrue(US41.partialDates("MAR1890"),"names match the list of decesaed")
        
    def test_subset(self):
        self.assertTrue(US41.partialDates("2000"),"Multiple names in list of deceased")

    def test_one_name(self):
        self.assertTrue(US41.partialDates("20AUG2024"),"One name in list of deceased")

    def test_no_match(self):
        self.assertTrue(US41.partialDates("1890"),"names not in list of deceased")

    def test_empty_list(self):
        self.assertFalse(US41.partialDates("12OCT19900"),"Empty List, False")

if __name__ == '__main__':
    unittest.main()
