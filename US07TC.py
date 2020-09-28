import unittest
import Team6TC
import copy

# Less than 150 years old
class TestStringMethods(unittest.TestCase):
    
    global result
    result = Team6TC.retrieveInfo()
    
    #Get the ouput from the Tables.txt file
    def test_result_good(self):
        self.assertTrue(Team6TC.less_than_150(result),"150 in list of ages from Tables.txt")
        
    def test_result_bad(self):
        temp = copy.deepcopy(result)
        temp.append('150')
        self.assertFalse(Team6TC.less_than_150(temp),"150 artificially added to the result of Tables.txt")
            
    def test_empty_list(self):
        self.assertFalse(Team6TC.less_than_150([]),"Empty List not True or False")
        
    def test_not_in_list(self):
        self.assertNotIn('150',result,"150 not in list of ages")
        
    def test_in_list(self):
        temp = copy.deepcopy(result)
        temp.append('150')
        self.assertIn('150',temp,"150 in list of ages")
        
    

if __name__ == '__main__':
    unittest.main()
