import unittest;
#
# User story for not marrying before 14.
# 
# Matthew Evanego
class TestUS9(unittest.TestCase):

    marriedDate = [3,4,1993]
    birthDate = [1, 5, 1960]
    #Ensures that person is not married before 14
    def marriedBefore14(self, marriedDate, birthDate):
        if(marriedDate[2] - birthDate[2] < 14):
            return False
        elif(marriedDate[2] - birthDate[2] == 14 and marriedDate[1] - birthDate[1] > 0 and marriedDate[0] - birthDate[0] > 0):
            return False
        return True

    #Testing both of the parents
    def test_marriedBefore14(self):
        marriedDate = [3, 4, 1993]
        birthDate = [1, 5, 1960]
        self.assertTrue(self.marriedBefore14(marriedDate, birthDate))
        marriedDate = [3,4,1970]
        self.assertFalse(self.marriedBefore14(marriedDate, birthDate))
        

        

if __name__ == '__main__':
    unittest.main()
        
