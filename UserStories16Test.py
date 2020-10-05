import unittest
import UserStories16

class TestStringMethods(unittest.TestCase):
    global MaleLastNames
    MaleLastNames = UserStories16.retrieveInfo()
    
    def test_empty(self):
        self.assertFalse(UserStories16.checkMaleLastNames([]),"There are no males")
    
    def test_type(self):
        self.assertIs(type(UserStories16.checkMaleLastNames(MaleLastNames)), list, "It is not a list type")

    def test_assert_isinstance(self):
        self.assertFalse(UserStories16.checkMaleLastNames("Diaz"), "It is not a list type")

    def test_assert_equals(self):
        allMaleLastNames = ['Diaz', 'Diaz', 'Diaz', 'Geronimo', 'Geronimo', 'Diaz', 'Pena', 'Pena', 'Pena', 'Diaz', 'Severino', 'Alayon', 'Alayon', 'Alayon', 'Alayon']
        self.assertEqual(UserStories16.checkMaleLastNames(MaleLastNames), allMaleLastNames)

    def test_first_element(self):
        allMaleLastNames = ['Diaz', 'Diaz', 'Diaz', 'Geronimo', 'Geronimo', 'Diaz', 'Pena', 'Pena', 'Pena', 'Diaz', 'Severino', 'Alayon', 'Alayon', 'Alayon', 'Alayon']
        self.assertEqual(UserStories16.checkMaleLastNames(MaleLastNames)[0], allMaleLastNames[0])

if __name__ == '__main__':
    unittest.main()