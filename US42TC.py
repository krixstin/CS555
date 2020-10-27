
import unittest
import US42

# Less than 150 years old
class TestStringMethods(unittest.TestCase):
   

    #Format (husband,wife)
    def test_century_leap_year(self):
        self.assertTrue(US42.illegitimate_dates("29FEB1600"),"Century Leap Year")
        
    def test_invalid_Feb(self):
        self.assertFalse(US42.illegitimate_dates("30FEB1600"),"Feb more than 3 days")
            
    def test_valid_CLY_Feb(self):
        self.assertTrue(US42.illegitimate_dates("10FEB1601"),"Non Century Leap Year Valid Date")
        
    def test_valid_date(self):
        self.assertTrue(US42.illegitimate_dates("01AUG2000"),"Husband is two times older")
        
    def test_invalid_CLY_Feb(self):
        self.assertFalse(US42.illegitimate_dates("29FEB1601"),"Not a Leap Year")
        
    def test_fail_on_same_year(self):
        self.assertFalse(US42.illegitimate_dates("32AUG2000"),"Invalid Normal Month")

if __name__ == '__main__':
    unittest.main()
