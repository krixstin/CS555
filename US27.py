# US27: Include person's current age when listing individuals
# Author: Kristin Kim

from datetime import date
from gedcom.parser import Parser
from gedcom.element.individual import IndividualElement

file_path = 'DiazJGedcomProject1.ged'

gedcom_parser = Parser()
gedcom_parser.parse_file(file_path, False)  # Disable strict parsing
elements = gedcom_parser.get_element_list()

today = date.today()
d4 = today.strftime("%d %b %Y").split(" ")  # ['09', 'Oct', '2020']
t_day = int(d4[0])
t_month = d4[1].upper()
t_year = d4[2]

month_list = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

t_month_int = month_list.index(t_month)+1  # JAN=1, FEB=2, DEC=12


n = []


def individual_age(a):

    root_child_elements = gedcom_parser.get_root_child_elements()

    for element in root_child_elements:

        if isinstance(element, IndividualElement):

            (first, last) = element.get_name()
            name = first + " " + last
            (date, place, source) = element.get_birth_data()
            # print(name)

            full = date.split(" ")
            day = int(full[0])
            month = full[1]
            month_int = month_list.index(month) + 1
            # print(month, month_int)
            year = int(full[2])

            age = int(t_year)-year

            if t_month_int < month_int:
                extra = 1;

            elif t_month_int == month_int and t_day > day:
                extra =1;

            else:
                extra = 0
            age = age+extra
            n.append((name, age))

    # print(n)

    if a in n:
        return True
    else:
        return False


# print(individual_age(('Javier Diaz', 20)))
