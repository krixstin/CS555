# US30: List living married
# Author: Kristin Kim

l=[]
# a is for unittest
def livingMarried(a):
    a=""
    for element in elements:

        if isinstance(element, IndividualElement):

            # check living
            if str(element.is_deceased()) == "False":  # getname individualclassElement
                (first, last) = element.get_name()

                # check marriagedate, if not N/A [], print
                marriageDates = gedcom_parser.get_marriages(element)

                if marriageDates!=[]:

                    # store in list l for unittest
                    l.append(str(first+" "+last))

                    # print living Married
                    print("Living & Married: "+ first + " " + last)
                else:
                    continue

    if a in l:
        return True
    else:
        return False
    
 
