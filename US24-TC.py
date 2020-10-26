import unittest
import US24


class US24TC(unittest.TestCase):

    def test_T_uniqueMarriages(self):
        self.assertTrue(US24.unique_spouses({
            '@F1@': [['HUSB', '@I2@', 'Miguel /Diaz/'], ['WIFE', '@I3@', 'Deysi /Geronimo/'],
                     ['CHIL', '@I1@', 'Javier /Diaz/'], ['CHIL', '@I4@', 'Xavier /Diaz/'],
                     ['MARR'], ['DATE', '16 SEP 1998'], ['DIV'], ['DATE', '13 APR 2006']],
            '@F2@': [['HUSB', '@I2@', 'Miguel /Diaz/'], ['WIFE', '@I17@', 'Maria /Santos/'],
                     ['CHIL', '@I15@', 'Miguel Adonis /Diaz/'], ['MARR'], ['DATE', '7 MAY 1995'],
                     ['_SEPR'], ['DATE', '18 OCT 1998']],
            '@F3@': [['HUSB', '@I9@', 'Federico /Diaz/'], ['WIFE', '@I10@', 'Elena /Cruz/'],
                     ['CHIL', '@I2@', 'Miguel /Diaz/'], ['CHIL', '@I21@', 'Iris /Diaz/'],
                     ['CHIL', '@I26@', 'Mercedes /Diaz/'], ['MARR'], ['DATE', '4 FEB 1965']],
            '@F4@': [['HUSB', '@I5@', 'Cesar /Geronimo/'], ['WIFE', '@I6@', 'Daisy /Guerrero/'],
                     ['CHIL', '@I3@', 'Deysi /Geronimo/'], ['CHIL', '@I7@', 'Cesar Jr /Geronimo/'],
                     ['CHIL', '@I8@', 'Cecilia /Geronimo/'], ['MARR'], ['DATE', '28 APR 1970']]
        }))

    def test_F_uniqueMarriages(self):
        self.assertFalse(US24.unique_spouses({
            '@F1@': [['HUSB', '@I2@', 'Miguel /Diaz/'], ['WIFE', '@I3@', 'Deysi /Geronimo/'],
                     ['CHIL', '@I1@', 'Javier /Diaz/'], ['CHIL', '@I4@', 'Xavier /Diaz/'], ['MARR'],
                     ['DATE', '16 SEP 1998'], ['DIV'], ['DATE', '13 APR 2006']],
            '@F2@': [['HUSB', '@I2@', 'Miguel /Diaz/'], ['WIFE', '@I17@', 'Maria /Santos/'],
                     ['CHIL', '@I15@', 'Miguel Adonis /Diaz/'], ['MARR'], ['DATE', '7 MAY 1995'], ['_SEPR'],
                     ['DATE', '18 OCT 1998']],
            '@F3@': [['HUSB', '@I9@', 'Federico /Diaz/'], ['WIFE', '@I10@', 'Elena /Cruz/'],
                     ['CHIL', '@I2@', 'Miguel /Diaz/'], ['CHIL', '@I21@', 'Iris /Diaz/'],
                     ['CHIL', '@I26@', 'Mercedes /Diaz/'], ['MARR'], ['DATE', '4 FEB 1965']],
            '@F4@': [['HUSB', '@I5@', 'Federico /Diaz/'], ['WIFE', '@I6@', 'Elena /Cruz/'],
                     ['CHIL', '@I3@', 'Deysi /Geronimo/'], ['CHIL', '@I7@', 'Cesar Jr /Geronimo/'],
                     ['CHIL', '@I8@', 'Cecilia /Geronimo/'], ['MARR'], ['DATE', '4 FEB 1965']]
        }))


if __name__ == '__main__':
    unittest.main()
