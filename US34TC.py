
import unittest
import US34

# Less than 150 years old
class TestStringMethods(unittest.TestCase):
   

    #Format (husband,wife)
    def test_result_good(self):
        self.assertFalse(US34.large_age_diff("10MAR1890","10MAR1890", "22JUN2010"),"Same age")
        
    def test_result_same_year_diff_month(self):
        self.assertFalse(US34.large_age_diff("10MAR2000","27AUG2000", "22JUN1000"),"Wedding before birth of partners")
            
    def test_result_same_year_same_month_diff_day(self):
        self.assertFalse(US34.large_age_diff("10MAR2000","27AUG2022", "22JUN3000"),"Diiferent ages")
        
    def test_marrige_before_birth(self):
        self.assertTrue(US34.large_age_diff("10MAR1890","27AUG1990", "22JUN2010"),"Husband is two times older")
        
    def test_fail_on_same_year(self):
        self.assertTrue(US34.large_age_diff("10MAR1990","27AUG1890", "22JUN2010"),"Wife is two days older")

if __name__ == '__main__':
    unittest.main()
