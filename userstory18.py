import unittest;
#
# User story for siblings not marrying.
# 
# Matthew Evanego
class TestUS18(unittest.TestCase):

    #Ensures that siblings are not married.
    def siblingsMarried(self, siblings, hwIDS):
        for hwPair in hwIDS:
            for sibs in siblings:
                ID1 = hwPair[0]
                ID2 = hwPair[1]
                if(ID1 in sibs and ID2 in sibs):
                    return False
        return True

    #Testing both of the parents
    def test_sibsMarried(self):
        siblings = [['I1', 'I2'], ['I3', 'I4']]
        hwIDS = [['I1', 'I5'], ['I3', 'I4']]
        self.assertFalse(self.siblingsMarried(siblings, hwIDS))
        hwIDS = [['I1', 'I5'], ['I3', 'I8']]
        self.assertTrue(self.siblingsMarried(siblings, hwIDS))

        

if __name__ == '__main__':
    unittest.main()
        
