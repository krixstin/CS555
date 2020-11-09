import unittest;

# User Story for Divorce Before Death
# Matthew Evanego
class TestUS6(unittest.TestCase):

    #Param: death_date [day, month, year] | divorce_date [day, month, year]
    def divorce_before_death(self, death_date1, death_date2, divorce_date):
        if(divorce_date[2] < death_date1[2] and divorce_date[2] < death_date2[2]):
            return True
        elif(divorce_date[2] <= death_date1[2] and divorce_date[2] <= death_date2[2] and divorce_date[1] < death_date2[1] and divorce_date[1] < death_date1[1]):
            return True
        elif(divorce_date[2] <= death_date1[2] and divorce_date[2] <= death_date2[2] and divorce_date[1] <= death_date2[1] and divorce_date[1] <= death_date1[1] and divorce_date[0] < death_date1[0] and divorce_date[0] < death_date2[0]):
            return True
        return False

    def test_divorce_before_death(self):
        death_date1 = [1,1,1990]
        death_date2 = [1,1,1990]
        divorceDate = [1,1,2000]
        self.assertFalse(self.divorce_before_death(death_date1, death_date2, divorceDate))

        death_date1 = [1,1,2000]
        death_date2 = [1,1,1990]
        divorceDate = [1,1,1995]
        self.assertFalse(self.divorce_before_death(death_date1, death_date2, divorceDate))

        death_date1 = [1,2,2000]
        death_date2 = [1,2,2000]
        divorceDate = [1,1,2000]
        self.assertTrue(self.divorce_before_death(death_date1, death_date2, divorceDate))

        death_date1 = [4,2,2000]
        death_date2 = [1,7,2000]
        divorceDate = [7,7,2000]
        self.assertFalse(self.divorce_before_death(death_date1, death_date2, divorceDate))


if __name__ == '__main__':
    unittest.main()