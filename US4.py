import unittest;

# User Story for Marriage Before Divorce
# Matthew Evanego
class TestUS4(unittest.TestCase):

    #Param: marriage_date [day, month, year] | divorce_date [day, month, year]
    def married_before_divorced(self, marriage_date, divorce_date):
        if(marriage_date[2] < divorce_date[2]):
            return True
        elif(marriage_date[2] == divorce_date[2] and marriage_date[1] == divorce_date[1] and marriage_date[0] == divorce_date[0]):
            return False
        elif(marriage_date[2] == divorce_date[2] and marriage_date[1] <= divorce_date[1] and marriage_date[0] <= divorce_date[0]):
            return True
        return False

    def test_marriage_before_divorce(self):
        marriageDate = [1,1,1990]
        divorceDate = [1,1,2000]
        self.assertTrue(self.married_before_divorced(marriageDate, divorceDate))

        marriageDate = [1,1,1995]
        divorceDate = [1,1,1990]
        self.assertFalse(self.married_before_divorced(marriageDate, divorceDate))

        marriageDate = [1,1,1995]
        divorceDate = [1,1,1995]
        self.assertFalse(self.married_before_divorced(marriageDate, divorceDate))

        marriageDate = [1,1,1995]
        divorceDate = [1,10,1995]
        self.assertTrue(self.married_before_divorced(marriageDate, divorceDate))

        marriageDate = [1,1,1995]
        divorceDate = [10,1,1995]
        self.assertTrue(self.married_before_divorced(marriageDate, divorceDate))


if __name__ == '__main__':
    unittest.main()