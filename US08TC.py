import unittest
import US08

# Less than 150 years old
class TestStringMethods(unittest.TestCase):
   

    #Format (birth_date,marrige_date)
    def test_result_good(self):
        self.assertTrue(US08.birth_before_marrige("7MAY1999","7MAY1998"),"Child born year earlier than marriage year")
        
    def test_result_same_year_diff_month(self):
        self.assertTrue(US08.birth_before_marrige("7MAY1999","7JAN1999"),"Child born year and marriage year equal, but child born month is earlier")
            
    def test_result_same_year_same_month_diff_day(self):
        self.assertTrue(US08.birth_before_marrige("27AUG2000","26AUG2000"),"Child born year/month and marriage year/month equal, but child born day is earlier")
        
    def test_marrige_before_birth(self):
        self.assertFalse(US08.birth_before_marrige("4SEP2000","6APR2010"),"Marrige date after birth of child")
        
    def test_fail_on_same_year(self):
        self.assertFalse(US08.birth_before_marrige("14MAR2010","20DEC2010"),"Marrige date after birth of child")

    def test_fail_on_same_year_same_month(self):
        self.assertFalse(US08.birth_before_marrige("14DEC2010","20DEC2010"),"Marrige date after birth of child")
        
    

if __name__ == '__main__':
    unittest.main()