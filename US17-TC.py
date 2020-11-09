import unittest
import US17

class MyTestCase(unittest.TestCase):
    global FAM
    global FAM_F

    FAM = {
        '@F1@': [['HUSB', '@I2@', 'Miguel /Diaz/'], ['WIFE', '@I3@', 'Deysi /Geronimo/'],
                 ['CHIL', '@I1@', 'Javier /Diaz/'], ['CHIL', '@I4@', 'Xavier /Diaz/'], ['MARR'],
                 ['DATE', '16 SEP 1998'], ['DIV'], ['DATE', '13 APR 2006']],
        '@F2@': [['HUSB', '@I2@', 'Miguel /Diaz/'], ['WIFE', '@I17@', 'Maria /Santos/'],
                 ['CHIL', '@I15@', 'Miguel Adonis /Diaz/'], ['MARR'], ['DATE', '7 MAY 1995'], ['_SEPR'],
                 ['DATE', '18 OCT 1998']],
        '@F3@': [['HUSB', '@I9@', 'Federico /Diaz/'], ['WIFE', '@I10@', 'Elena /Cruz/'],
                 ['CHIL', '@I2@', 'Miguel /Diaz/'], ['CHIL', '@I21@', 'Iris /Diaz/'],
                 ['CHIL', '@I26@', 'Mercedes /Diaz/'], ['MARR'], ['DATE', '4 FEB 1965']],
        '@F4@': [['HUSB', '@I5@', 'Cesar /Geronimo/'], ['WIFE', '@I6@', 'Daisy /Guerrero/'],
                 ['CHIL', '@I3@', 'Deysi /Geronimo/'], ['CHIL', '@I7@', 'Cesar Jr /Geronimo/'],
                 ['CHIL', '@I8@', 'Cecilia /Geronimo/'], ['MARR'], ['DATE', '28 APR 1970']],
        '@F5@': [['HUSB', '@I7@', 'Cesar Jr /Geronimo/'], ['WIFE', '@I16@', 'Stephanie /Gonzalez/'],
                 ['CHIL', '@I18@', 'Gabriela /Geronimo/'], ['MARR'], ['DATE', '9 MAY 2010'], ['DIV'],
                 ['DATE', '11 SEP 2013']],
        '@F6@': [['HUSB', '@I7@', 'Cesar Jr /Geronimo/'], ['WIFE', '@I19@', 'Ana /Castro/'],
                 ['CHIL', '@I20@', 'Ginelly /Geronimo/'], ['MARR'], ['DATE', '4 FEB 2018'], ['_SEPR'],
                 ['DATE', '9 JUL 2019']],
        '@F7@': [['HUSB', '@I11@', 'Donny /Pena/'], ['WIFE', '@I8@', 'Cecilia /Geronimo/'],
                 ['CHIL', '@I12@', 'Daileen /Pena/'], ['CHIL', '@I13@', 'Derek /Pena/'],
                 ['CHIL', '@I14@', 'Dariel /Pena/'], ['MARR'], ['DATE', '7 JAN 2000']],
        '@F8@': [['HUSB', '@I22@', 'Luis /Severino/'], ['WIFE', '@I21@', 'Iris /Diaz/'],
                 ['CHIL', '@I23@', 'Karen /Severino/'], ['CHIL', '@I24@', 'Karol /Severino/'],
                 ['CHIL', '@I25@', 'Katy /Severino/'], ['MARR'], ['DATE', '25 JUN 1999']],
        '@F9@': [['HUSB', '@I27@', 'Carlos /Alayon/'], ['WIFE', '@I26@', 'Mercedes /Diaz/'],
                 ['CHIL', '@I28@', 'Emilkar /Alayon/'], ['CHIL', '@I29@', 'Fredrick /Alayon/'],
                 ['CHIL', '@I30@', 'Emil /Alayon/'], ['MARR'], ['DATE', '22 FEB 1984']]
    }

    FAM_F = {
        '@F1@': [['HUSB', '@I2@', 'Miguel /Diaz/'], ['WIFE', '@I3@', 'Deysi /Geronimo/'],
                 ['CHIL', '@I1@', 'Javier /Diaz/'], ['CHIL', '@I3@', 'Xavier /Diaz/'], ['MARR'],
                 ['DATE', '16 SEP 1998'], ['DIV'], ['DATE', '13 APR 2006']],
        '@F2@': [['HUSB', '@I2@', 'Miguel /Diaz/'], ['WIFE', '@I17@', 'Maria /Santos/'],
                 ['CHIL', '@I15@', 'Miguel Adonis /Diaz/'], ['MARR'], ['DATE', '7 MAY 1995'], ['_SEPR'],
                 ['DATE', '18 OCT 1998']],
        '@F3@': [['HUSB', '@I9@', 'Federico /Diaz/'], ['WIFE', '@I10@', 'Elena /Cruz/'],
                 ['CHIL', '@I2@', 'Miguel /Diaz/'], ['CHIL', '@I21@', 'Iris /Diaz/'],
                 ['CHIL', '@I26@', 'Mercedes /Diaz/'], ['MARR'], ['DATE', '4 FEB 1965']],
        '@F4@': [['HUSB', '@I5@', 'Cesar /Geronimo/'], ['WIFE', '@I6@', 'Daisy /Guerrero/'],
                 ['CHIL', '@I3@', 'Deysi /Geronimo/'], ['CHIL', '@I7@', 'Cesar Jr /Geronimo/'],
                 ['CHIL', '@I8@', 'Cecilia /Geronimo/'], ['MARR'], ['DATE', '28 APR 1970']],
        '@F5@': [['HUSB', '@I7@', 'Cesar Jr /Geronimo/'], ['WIFE', '@I16@', 'Stephanie /Gonzalez/'],
                 ['CHIL', '@I18@', 'Gabriela /Geronimo/'], ['MARR'], ['DATE', '9 MAY 2010'], ['DIV'],
                 ['DATE', '11 SEP 2013']],
        '@F6@': [['HUSB', '@I7@', 'Cesar Jr /Geronimo/'], ['WIFE', '@I19@', 'Ana /Castro/'],
                 ['CHIL', '@I20@', 'Ginelly /Geronimo/'], ['MARR'], ['DATE', '4 FEB 2018'], ['_SEPR'],
                 ['DATE', '9 JUL 2019']],
        '@F7@': [['HUSB', '@I11@', 'Donny /Pena/'], ['WIFE', '@I8@', 'Cecilia /Geronimo/'],
                 ['CHIL', '@I12@', 'Daileen /Pena/'], ['CHIL', '@I13@', 'Derek /Pena/'],
                 ['CHIL', '@I14@', 'Dariel /Pena/'], ['MARR'], ['DATE', '7 JAN 2000']],
        '@F8@': [['HUSB', '@I22@', 'Luis /Severino/'], ['WIFE', '@I21@', 'Iris /Diaz/'],
                 ['CHIL', '@I23@', 'Karen /Severino/'], ['CHIL', '@I24@', 'Karol /Severino/'],
                 ['CHIL', '@I25@', 'Katy /Severino/'], ['MARR'], ['DATE', '25 JUN 1999']],
        '@F9@': [['HUSB', '@I27@', 'Carlos /Alayon/'], ['WIFE', '@I26@', 'Mercedes /Diaz/'],
                 ['CHIL', '@I28@', 'Emilkar /Alayon/'], ['CHIL', '@I29@', 'Fredrick /Alayon/'],
                 ['CHIL', '@I30@', 'Emil /Alayon/'], ['MARR'], ['DATE', '22 FEB 1984']]
    }

    def test_T_PandCMarrige(self):
        self.assertTrue(US17.parentsNotMarriedToChildren(FAM))

    def test_F_PandCMarrige(self):
        self.assertFalse(US17.parentsNotMarriedToChildren(FAM_F))


if __name__ == '__main__':
    unittest.main()
