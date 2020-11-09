import unittest
import US13


class MyTestCase(unittest.TestCase):

    global INDI
    global INDI_F
    global FAM
    INDI = {
        '@I1@': ['Javier /Diaz/', 'M', '27 AUG 2000', 20, True, 'N/A', ['@F1@', 'N/A']],
        '@I2@': ['Miguel /Diaz/', 'M', '9 SEP 1967', 53, True, 'N/A', ['N/A', '@F1@'], ['N/A', '@F2@'],
                 ['@F3@', 'N/A']],
        '@I3@': ['Deysi /Geronimo/', 'F', '3 JAN 1979', 41, True, 'N/A', ['N/A', '@F1@'], ['@F4@', 'N/A']],
        '@I4@': ['Xavier /Diaz/', 'M', '27 AUG 2000', 20, True, 'N/A', ['@F1@', 'N/A']],
        '@I5@': ['Cesar /Geronimo/', 'M', '23 MAY 1944', 76, True, 'N/A', ['N/A', '@F4@']],
        '@I6@': ['Daisy /Guerrero/', 'F', '25 APR 1953', 67, True, 'N/A', ['N/A', '@F4@']],
        '@I7@': ['Cesar Jr /Geronimo/', 'M', '9 SEP 1977', 43, True, 'N/A', ['@F4@', 'N/A'], ['N/A', '@F5@'],
                 ['N/A', '@F6@']],
        '@I8@': ['Cecilia /Geronimo/', 'F', '4 DEC 1982', 38, True, 'N/A', ['@F4@', 'N/A'], ['N/A', '@F7@']],
        '@I9@': ['Federico /Diaz/', 'M', '9 DEC 1936', 84, False, '11 MAR 1985', ['N/A', '@F3@']],
        '@I10@': ['Elena /Cruz/', 'F', '14 JUL 1940', 80, True, 'N/A', ['N/A', '@F3@']],
        '@I11@': ['Donny /Pena/', 'M', '20 FEB 1978', 42, True, 'N/A', ['N/A', '@F7@']],
        '@I12@': ['Daileen /Pena/', 'F', '18 JUN 2002', 18, True, 'N/A', ['@F7@', 'N/A']],
        '@I13@': ['Derek /Pena/', 'M', '4 OCT 2004', 16, True, 'N/A', ['@F7@', 'N/A']],
        '@I14@': ['Dariel /Pena/', 'M', '17 JUN 2009', 11, True, 'N/A', ['@F7@', 'N/A']],
        '@I15@': ['Miguel Adonis /Diaz/', 'M', '20 MAR 1997', 23, True, 'N/A', ['@F2@', 'N/A']],
        '@I16@': ['Stephanie /Gonzalez/', 'F', '13 JUN 1980', 40, True, 'N/A', ['N/A', '@F5@']],
        '@I17@': ['Maria /Santos/', 'F', '12 OCT 1969', 51, False, '18 OCT 1998', ['N/A', '@F2@']],
        '@I18@': ['Gabriela /Geronimo/', 'F', '12 AUG 2007', 13, False, '3 DEC 2014', ['@F5@', 'N/A']],
        '@I19@': ['Ana /Castro/', 'F', '9 OCT 1979', 41, True, 'N/A', ['N/A', '@F6@']],
        '@I20@': ['Ginelly /Geronimo/', 'F', '3 JUN 2018', 2, True, 'N/A', ['@F6@', 'N/A']],
        '@I21@': ['Iris /Diaz/', 'F', '16 SEP 1976', 44, True, 'N/A', ['@F3@', 'N/A'], ['N/A', '@F8@']],
        '@I22@': ['Luis /Severino/', 'M', '30 JUN 1970', 50, True, 'N/A', ['N/A', '@F8@']],
        '@I23@': ['Karen /Severino/', 'F', '13 JUL 2002', 18, True, 'N/A', ['@F8@', 'N/A']],
        '@I24@': ['Karol /Severino/', 'F', '10 NOV 2004', 16, True, 'N/A', ['@F8@', 'N/A']],
        '@I25@': ['Katy /Severino/', 'F', '24 JAN 2008', 12, True, 'N/A', ['@F8@', 'N/A']],
        '@I26@': ['Mercedes /Diaz/', 'F', '30 SEP 1970', 50, True, 'N/A', ['@F3@', 'N/A'], ['N/A', '@F9@']],
        '@I27@': ['Carlos /Alayon/', 'M', '13 OCT 1965', 55, True, 'N/A', ['N/A', '@F9@']],
        '@I28@': ['Emilkar /Alayon/', 'M', '30 SEP 1985', 35, True, 'N/A', ['@F9@', 'N/A']],
        '@I29@': ['Fredrick /Alayon/', 'M', '21 DEC 1990', 30, True, 'N/A', ['@F9@', 'N/A']],
        '@I30@': ['Emil /Alayon/', 'M', '23 JAN 2001', 19, True, 'N/A', ['@F9@', 'N/A']]
    }

    INDI_F = {
        '@I1@': ['Javier /Diaz/', 'M', '27 AUG 2000', 20, True, 'N/A', ['@F1@', 'N/A']],
        '@I2@': ['Miguel /Diaz/', 'M', '9 SEP 1967', 53, True, 'N/A', ['N/A', '@F1@'], ['N/A', '@F2@'],
                 ['@F3@', 'N/A']],
        '@I3@': ['Deysi /Geronimo/', 'F', '3 JAN 1979', 41, True, 'N/A', ['N/A', '@F1@'], ['@F4@', 'N/A']],
        '@I4@': ['Xavier /Diaz/', 'M', '27 MAY 2000', 20, True, 'N/A', ['@F1@', 'N/A']],
        '@I5@': ['Cesar /Geronimo/', 'M', '23 MAY 1944', 76, True, 'N/A', ['N/A', '@F4@']],
        '@I6@': ['Daisy /Guerrero/', 'F', '25 APR 1953', 67, True, 'N/A', ['N/A', '@F4@']],
        '@I7@': ['Cesar Jr /Geronimo/', 'M', '9 SEP 1977', 43, True, 'N/A', ['@F4@', 'N/A'], ['N/A', '@F5@'],
                 ['N/A', '@F6@']],
        '@I8@': ['Cecilia /Geronimo/', 'F', '4 DEC 1982', 38, True, 'N/A', ['@F4@', 'N/A'], ['N/A', '@F7@']],
        '@I9@': ['Federico /Diaz/', 'M', '9 DEC 1936', 84, False, '11 MAR 1985', ['N/A', '@F3@']],
        '@I10@': ['Elena /Cruz/', 'F', '14 JUL 1940', 80, True, 'N/A', ['N/A', '@F3@']],
        '@I11@': ['Donny /Pena/', 'M', '20 FEB 1978', 42, True, 'N/A', ['N/A', '@F7@']],
        '@I12@': ['Daileen /Pena/', 'F', '18 JUN 2002', 18, True, 'N/A', ['@F7@', 'N/A']],
        '@I13@': ['Derek /Pena/', 'M', '4 OCT 2004', 16, True, 'N/A', ['@F7@', 'N/A']],
        '@I14@': ['Dariel /Pena/', 'M', '17 JUN 2009', 11, True, 'N/A', ['@F7@', 'N/A']],
        '@I15@': ['Miguel Adonis /Diaz/', 'M', '20 MAR 1997', 23, True, 'N/A', ['@F2@', 'N/A']],
        '@I16@': ['Stephanie /Gonzalez/', 'F', '13 JUN 1980', 40, True, 'N/A', ['N/A', '@F5@']],
        '@I17@': ['Maria /Santos/', 'F', '12 OCT 1969', 51, False, '18 OCT 1998', ['N/A', '@F2@']],
        '@I18@': ['Gabriela /Geronimo/', 'F', '12 AUG 2007', 13, False, '3 DEC 2014', ['@F5@', 'N/A']],
        '@I19@': ['Ana /Castro/', 'F', '9 OCT 1979', 41, True, 'N/A', ['N/A', '@F6@']],
        '@I20@': ['Ginelly /Geronimo/', 'F', '3 JUN 2018', 2, True, 'N/A', ['@F6@', 'N/A']],
        '@I21@': ['Iris /Diaz/', 'F', '16 SEP 1976', 44, True, 'N/A', ['@F3@', 'N/A'], ['N/A', '@F8@']],
        '@I22@': ['Luis /Severino/', 'M', '30 JUN 1970', 50, True, 'N/A', ['N/A', '@F8@']],
        '@I23@': ['Karen /Severino/', 'F', '13 JUL 2002', 18, True, 'N/A', ['@F8@', 'N/A']],
        '@I24@': ['Karol /Severino/', 'F', '10 NOV 2004', 16, True, 'N/A', ['@F8@', 'N/A']],
        '@I25@': ['Katy /Severino/', 'F', '24 JAN 2008', 12, True, 'N/A', ['@F8@', 'N/A']],
        '@I26@': ['Mercedes /Diaz/', 'F', '30 SEP 1970', 50, True, 'N/A', ['@F3@', 'N/A'], ['N/A', '@F9@']],
        '@I27@': ['Carlos /Alayon/', 'M', '13 OCT 1965', 55, True, 'N/A', ['N/A', '@F9@']],
        '@I28@': ['Emilkar /Alayon/', 'M', '30 SEP 1985', 35, True, 'N/A', ['@F9@', 'N/A']],
        '@I29@': ['Fredrick /Alayon/', 'M', '21 DEC 1990', 30, True, 'N/A', ['@F9@', 'N/A']],
        '@I30@': ['Emil /Alayon/', 'M', '23 JAN 2001', 19, True, 'N/A', ['@F9@', 'N/A']]
    }

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

    def test_T_birth_child(self):
        self.assertTrue(US13.childbirths(FAM, INDI))

    def test_F_birth_child(self):
        self.assertFalse(US13.childbirths(FAM, INDI_F))

if __name__ == '__main__':
    unittest.main()
