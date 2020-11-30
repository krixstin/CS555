# US43 List Generation Z
# List all living people that were born between 1997 and 2012
# Author: Kristin Kim

from gedcom.parser import Parser
from gedcom.element.individual import IndividualElement

file_path = 'DiazJGedcomProject1.ged'

gedcom_parser = Parser()
gedcom_parser.parse_file(file_path, False)  # Disable strict parsing
elements = gedcom_parser.get_element_list()


def gen_z(a):
    l = []

    for element in elements:

        if isinstance(element, IndividualElement):

            if str(element.is_deceased()) == "False":  # get_ame individualclassElement
                (first, last) = element.get_name()
                name = first+" "+last
                year = element.get_birth_year()

                if 1997 <= year <= 2012:
                        l.append(name)
                        l.append(year)
                        print(first + " " + last + " is  Generation Z")

    # print("\n", l)  # name and date

    if a in l:
        return True
    else:
        return False


# print(gen_z("Emil Alayon"))    # check if name is in list l

