# US36: List all people in a GEDCOM file who died in the last 30 days
# Author: Kristin Kim
"""
comment out line 26 (month), 27 (day), 28(year) to get the real data. This is set as 23 DEC 2014 for unittest
"""

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
index = month_list.index(t_month)

index = 11  # December
t_day = 23
t_year = 2014

d = []


def recent_death(a):

    root_child_elements = gedcom_parser.get_root_child_elements()

    for element in root_child_elements:

        if isinstance(element, IndividualElement):

            if str(element.is_deceased()) == "True":
                (first, last) = element.get_name()
                name = first + " " + last
                (date, place, source) = element.get_death_data()

                full = date.split(" ")
                day = int(full[0])
                month = full[1]
                year = int(full[2])

                if year == t_year:
                    if  month == month_list[index] and day < t_day:
                        # store in list l for unittest
                        d.append(name)
                        d.append(date)
                        print("Deceased: "+first + " " + last+" on "+date)

                    # DEC JAN
                    if  (year == t_year+1 and month_list[index] == "DEC") and  day > t_day:
                        d.append(name)
                        d.append(date)
                        print("Deceased: " + first + " " + last + " on " + date)
            else:
                continue
    # print(d)
    if a in d:
        return True
    else:
        return False


print(recent_death("Gabriela Geronimo"))
