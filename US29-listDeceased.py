# US29: List deceased 
# Author: Kristin Kim

d=[]
def listDeceased(a):
    a=""
    root_child_elements = gedcom_parser.get_root_child_elements()

    for element in root_child_elements:

        if isinstance(element, IndividualElement):

            if str(element.is_deceased())=="True":
                (first, last) = element.get_name()

                # store in list l for unittest
                d.append(str(first + " " + last))

                print("Deceased: "+first + " " + last)
            else:
                continue

    if a in d:
        return True
    else:
        return False

