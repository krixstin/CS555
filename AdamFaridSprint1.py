
# unit test case 
import unittest 
import collections
import sys


f = open("AdamFarid.ged", "r")
nameArr = []
birthDate = []
for line in f:
    names = line.split(" ")
    if "NAME" in line:
        ans = " ".join(names[2:])
        nameArr.append(ans)
    if "DATE" in line:
        dates = " ".join(names[2:])
        birthDate.append(dates)
    
checkNames = collections.Counter(nameArr)
checkDates = collections.Counter(birthDate)
def is_unique_name(name):
    name = "".join(name)
    if name == None:
        return False
    if name not in nameArr:
        return False
    else:
        if(checkNames[name] > 1):
            return False
        else:
            return True

def is_unique_date(date=None):
    if date == None:
        return False
    date = "".join(date)
    if date not in birthDate:
        return False
    else:
        if(checkDates[date] > 1):
            return False
        else:
            return True



class TestStringMethods(unittest.TestCase):

    def test_unique(self):
        self.assertTrue(is_unique_name(['Deysi /Geronimo/\n']))

    def test_1_item(self):
        self.assertTrue(is_unique_name(['Xavier /Diaz/\n']))

    def test_no_item(self):
        self.assertFalse(is_unique_date())

    def test_date(self):
        self.assertTrue(is_unique_date(['20 MAR 1997\n']))

    def test_multi_date(self):
        self.assertFalse(is_unique_date(['27 AUG 2000\n']))


if __name__ == '__main__':
    unittest.main()
