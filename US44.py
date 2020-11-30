# US44 List Anniversaries Recently past
# List all living couples in a GEDCOM file whose marriage anniversaries recently occurred in last 30 days
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

month_list = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
index = month_list.index(t_month)

index = 4  # May
t_day = 10


# a is for unittest / check name is in the list
def recent_past_marriage(a):
    l = []

    # DO NOT PUT THIS a = ""
    for element in elements:

        if isinstance(element, IndividualElement):

            # check living
            if str(element.is_deceased()) == "False":  # get_ame individualclassElement
                (first, last) = element.get_name()
                name = first+" "+last
                # check marriage date, if not N/A [], print
                marriage_dates = gedcom_parser.get_marriages(element)

                if marriage_dates != []:
                    str_full = marriage_dates[0][0]
                    full = (marriage_dates[0][0]).split(" ")  #list
                    day = int(full[0])
                    month = full[1]

                    if month == month_list[index]:
                        if day < t_day:

                            l.append(name)
                            l.append(str_full)
                            # print(first + " " + last + "'s, " + str_full[:] + " wad in the last 30 days")

                    elif month == month_list[index-1]:
                        if day > t_day:
                            l.append(name)
                            l.append(str_full)
                            # print(first + " " + last + "'s, " + str_full[:] + " was in the last 30 days")

    # print("\n", l)  # name and date

    if a in l:
        return True
    else:
        return False


# print(recent_past_marriage("Cesar Geronimo"))    # check if name is in list l

