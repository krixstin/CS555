#  Author: Team 6
#  Name: Project 2
#  Date: September 14th, 2020
from gedcom.parser import Parser
from datetime import date
from prettytable import PrettyTable
from gedcom.element.element import Element
from gedcom.element.individual import IndividualElement
from gedcom.element.family import FamilyElement
import UniqueChecker
import sys
from datetime import datetime as dt
import datetime
from collections import Counter
import pandas

def check_ages(self, fathers, mothers):
    for childrenAge in fathers[0]:
        if fathers[1] - 80 > childrenAge:
            return False
    for childrenAge in mothers[0]:
        if mothers[1] - 60 > childrenAge:
            return False
    return True


today = date.today()
date = "{}/{}/{}".format(today.year, today.month, today.day)

VALID_TAGS = [
    "INDI", "NAME", "SEX", "BIRT", "DEAT",
    "MARR", "HUSB", "WIFE", "CHIL", "DIV",
    "DATE", "HEAD", "TRIL", "NOTE", "FAMC",
    "FAMS", "FAM"
]

INDI_TAGS = [
    "INDI", "NAME", "SEX", "BIRT", "DEAT",
    "MARR", "HUSB", "WIFE", "CHIL", "DATE",
    "HEAD",
]

FAM_TAGS = [
    "FAMC", "FAMS", "FAM",
    "MARR", "DIV", "_SEPR"
]

MONTHS = [
    "JAN", "FEB", "MAR", "APR",
    "MAY", "JUN", "JUL", "AUG",
    "SEP", "OCT", "NOV", "DEC"
]

INDI_DICT = {}
FAM_DICT = {}
INDI_FAM = True
file_path = 'DiazJGedcomProject1.ged'  # Path to your `.ged` file

INDI_TABLE = PrettyTable()
FAM_TABLE = PrettyTable()
INDI_TABLE.field_names = ["ID", "Name", "Gender",
                          "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
FAM_TABLE.field_names = ["ID", "Married", "Divorced",
                         "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]

gedcom_parser = Parser()
gedcom_parser.parse_file(file_path, False)  # Disable strict parsing

elements = gedcom_parser.get_element_list()

root_child_elements = gedcom_parser.get_root_child_elements()


def convertGedcomDate(datestring):
    return dt.strptime(datestring, "%d %b %Y")


def processGedcom(file_path):
    """Helper function for reading GEDCOM files when unit testing"""
    gedcom_parser.parse_file(file_path, False)
    elements = gedcom_parser.get_element_list()
    root_child_elements = gedcom_parser.get_root_child_elements()

    for element in root_child_elements:
        if isinstance(element, IndividualElement):
            return element

def processGedcomFamily(file_path):
    """Helper function for reading GEDCOM files when unit testing"""
    gedcom_parser.parse_file(file_path, False)
    elements = gedcom_parser.get_element_list()
    root_child_elements = gedcom_parser.get_root_child_elements()

    for element in root_child_elements:
        if isinstance(element, FamilyElement):
            return element


def birthBeforeMarriage(individual):
    """US02 - Birth should occur before the marriage of an individual"""
    birthDate = individual.get_birth_data()[0]
    marriageDates = gedcom_parser.get_marriages(individual)

    if marriageDates and birthDate:
        earliestMarriageDate = (min(convertGedcomDate(
            date[0]) for date in marriageDates))
        birthDate = convertGedcomDate(birthDate)
        if earliestMarriageDate < birthDate:
            print(
                f"Error US02: Marriage of {individual.get_name()[0]} {individual.get_name()[1]} ({individual.get_pointer()}) occurs before their birth")
            return False
        else:
            return True
    return None


def birthBeforeDeath(individual):
    """US03 - Birth should occur before death death of an individual"""
    birthdate = individual.get_birth_data()[0]
    deathdate = individual.get_death_data()[0]
    if birthdate and deathdate:
        birthdate = convertGedcomDate(birthdate)
        deathdate = convertGedcomDate(deathdate)
        if deathdate < birthdate:
            print(
                f"Error US03: Death of {individual.get_name()[0]} {individual.get_name()[1]} ({individual.get_pointer()}) occurs before their birth")
            return False
        else:
            return True
    return None


def datesBeforeCurrentDate(individual):
    """US01 - Dates (birth, marriage, divorce, death) should not be after the current date"""
    birthdate = individual.get_birth_data()[0]
    deathdate = individual.get_death_data()[0]
    marriageDates = gedcom_parser.get_marriages(individual)

    fams = gedcom_parser.get_families(individual)
    childElements = [(fam.get_child_elements()) for fam in fams]

    divorceDates = []
    for elements in childElements:
        for element in elements:
            if element.get_tag() == "DIV":
                divorceDates.append(element.get_child_elements()[0].get_value())


    latestDivorceDate = max(convertGedcomDate(date)
                            for date in divorceDates) if divorceDates else None
    latestMarriageDate = max(convertGedcomDate(
        date[0]) for date in marriageDates) if marriageDates else None
    birthdate = convertGedcomDate(birthdate) if birthdate else None
    deathdate = convertGedcomDate(deathdate) if deathdate else None

    comparisonDates = [birthdate, deathdate,
                       latestMarriageDate, latestDivorceDate]

    if any(day > dt.now() for day in comparisonDates if day):
        print(
            f"Error US05: Date associated with {individual.get_name()[0]} {individual.get_name()[1]} ({individual.get_pointer()}) occurs after current date")
        return False
    else:
        return True


def marriageBeforeDeath(individual):
    """US05 - Marriage should occur before death of either spouse"""
    deathDate = individual.get_death_data()[0]
    marriageDates = gedcom_parser.get_marriages(individual)

    if marriageDates and deathDate:
        latestMarriageDate = (max(convertGedcomDate(
            date[0]) for date in marriageDates))
        deathDate = convertGedcomDate(deathDate)
        if latestMarriageDate > deathDate:
            print(
                f"Error US05: Marriage of {individual.get_name()[0]} {individual.get_name()[1]} ({individual.get_pointer()}) occurs after their death")
            return False
        else:
            return True


def noBigamy(individual):
    """US11 - Marriage should not occur during marriage to another spouse"""


    families = gedcom_parser.get_families(individual)

    marraigeDateRanges = []
    for family in families:
        marriageDate = None
        divorceDate = None
        for element in family.get_child_elements():
            if element.get_tag() == "MARR":
                marriageDate = convertGedcomDate(element.get_child_elements()[0].get_value())

            if element.get_tag() == "DIV":
                divorceDate = convertGedcomDate(element.get_child_elements()[0].get_value())

        if divorceDate == None:
            divorceDate = dt.now()

        marraigeDateRanges.append((marriageDate, divorceDate))
    
    marraigeDateIntervals = pandas.arrays.IntervalArray.from_tuples(marraigeDateRanges)

    if marraigeDateIntervals.is_non_overlapping_monotonic:
        return True
    else:
        print(
                f"Error US11: Marriage of {individual.get_name()[0]} {individual.get_name()[1]} ({individual.get_pointer()}) occurs during another marriage")
        return False


def multipleBirths(family):
    """US14 - No more than five siblings should be born at the same time"""

    children = gedcom_parser.get_family_members(family, 'FAMILY_MEMBERS_TYPE_CHILDREN')
    birthdays = []
    for child in children:
        birthdays.append(convertGedcomDate(child.get_birth_data()[0]))

    if len(birthdays) < 5:
        return True
    else:
        birthdayCounts = dict((i, birthdays.count(i)) for i in birthdays)
        if len({k:v for (k,v) in birthdayCounts.items() if v >= 5}) > 0:
            print(
                f"Error US14: More than 5 siblings born at once in {family.get_value()} family ({family.get_pointer()})")
            return False
        else:
            return True



for element in root_child_elements:
    if isinstance(element, IndividualElement):

        # check for errors
        birthBeforeMarriage(element)
        birthBeforeDeath(element)
        marriageBeforeDeath(element)
        datesBeforeCurrentDate(element)
        noBigamy(element)

    if isinstance(element, FamilyElement):
        multipleBirths(element)




# Iterate through all root child elements
output = []
ids = []
famID = []
key = ""
for line in range(len(elements)):

    # Turn to string and split by spaces replacing any unnecessary strings
    input_line = str(elements[line]).replace("\r\n", "")

    # Output 1
    copy = "--> {}\n".format(input_line.replace("\xef\xbb\xbf", ""))

    # Split to assign level and tag
    info = tuple(input_line.split(" "))
    level = str(info[0])
    tag = str(info[1])

    # Concatenate all remaining elements
    args = " ".join(info[2:])

    # Result
    output.append(copy)

    #  Output
    file = open("Project02Output.txt", "w")
    level = level[-1]
    # Line has either INDI or FAM
    if "INDI" == args or "FAM" == args:
        if level == "0" and args == "FAM":
            INDI_FAM = False
            # print(False)
        if tag not in INDI_DICT and INDI_FAM:
            key = tag
            INDI_DICT[key] = []
            ids.append(key)
        elif tag not in FAM_DICT:
            key = tag
            FAM_DICT[key] = []
            famID.append(key)
        output.append("<-- {}|{}|{}|{}\n".format(level, args, "Y", tag))

    # Unsupported Tags [1,DATE]/[2,NAME]
    elif (level == "1" and tag == "DATE") or (level == "2" and tag == "NAME"):
        output.append("<-- {}|{}|{}|{}\n".format(level, tag, "N", args))

    # Line only has a level and tag, no arguments
    elif args == "":
        output.append("<-- {}|{}|{}\n".format(level, tag,
                                              "Y" if tag in VALID_TAGS else "N"))
        if tag in FAM_TAGS:
            FAM_DICT[key].append([tag])

    # Normal line with a level, tag, and arguments
    elif tag in INDI_TAGS:
        if INDI_FAM:
            # ["ID","Name","Gender","Birthday","Age","Alive","Death","Child","Spouse"]
            if tag == "DATE":
                x = args.split(" ")
                day = int(x[0])
                month = int(MONTHS.index(x[1]) + 1)
                year = int(x[2])
                INDI_DICT[key].append(args)

                age = today.year - year
                older = False
                if today.month - month > 0:
                    older = True
                elif today.month - month == 0:
                    if (today.month - month) >= 0:
                        older = True
                args = age

            # Check for Deaths
            if len(INDI_DICT[key]) > 4 and INDI_DICT[key][-2] == "Y":
                continue

            INDI_DICT[key].append(args)
        else:
            # print(key,tag,args,1)
            if tag == "DATE" or tag == "DIV":
                FAM_DICT[key].append([tag, args])
            else:
                if tag in ["HUSB", "WIFE"]:
                    INDI_DICT[args].append(["N/A", key])
                elif tag == "CHIL":
                    INDI_DICT[args].append([key, "N/A"])
            # First Fam tag found
            #["ID","Married","Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
            if args[0] != '@':
                continue

            FAM_DICT[key].append([tag, args, INDI_DICT[args][0]])
        # print(tag)
    else:
        output.append("<-- {}|{}|{}|{}\n".format(level, tag,
                                                 "Y" if tag in VALID_TAGS else "N", args))

# Print Table 1
file.writelines(output)
print("Outputted to Project02Output.txt file\n")
for x, y in INDI_DICT.items():

    if "Y" in y:
        y.remove("Y")
        y.insert(4, False)
    else:
        y.insert(4, True)
        y.insert(5, "N/A")

    body = y[0:6]
    rel = y[6:]
    body.insert(0, x.replace("@", ""))
    spouse = []
    child = ""
    for x in range(len(rel)):
        child = rel[x][0].replace("@", "")
        if (child == "N/A"):
            spouse.append(rel[x][1].replace("@", ""))
        else:
            body.append(child)

    while len(body) != 8:
        body.append([])

    body.append(spouse)
    INDI_TABLE.add_row(body)

print("Individuals")
print(INDI_TABLE)


# Print Table 2
output2 = []
result = []
for x, y in FAM_DICT.items():
    output2 = []
    output2.append(x.replace("@", ""))

    # Marriage Date
    if y.count(["MARR"]) > 0:
        #print(y[y.index(["MARR"]) + 1])
        output2.append(y[y.index(["MARR"]) + 1][1])

    # Divorced
    if y.count(["DIV"]) > 0:
        # Yes
        #print(y[y.index(["DIV"]) + 1][1])
        output2.append(y[y.index(["DIV"]) + 1][1])
    else:
        # No
        output2.append("N/A")

    # Husband ID
    husbID = y[0][1].replace("@", "")
    husbName = y[0][2]
    wifeID = y[1][1].replace("@", "")
    wifeName = y[1][2]
    output2.append(husbID)
    output2.append(husbName)
    output2.append(wifeID)
    output2.append(wifeName)

    children = []
    for x in y:
        if len(x) == 3:
            if x[0] == "CHIL":

                #print(x[1])
                children.append(x[1].replace("@",""))
        #print(children)
    #Checks for unique names and birthdays
    if not UniqueChecker.uniqueFirstNameFam(children, INDI_DICT):
        print("Children do not have unique names and birthdays")
    #Checks for unique IDs
    if not UniqueChecker.uniqueID(ids):
        print("Individuals do not have unique IDs")
    if not UniqueChecker.uniqueID(famID):
        print("Families do not have unique IDs")
    #User Story 15, Children cannot have more than 15 siblings
    if len(children) > 15:
        print("Greater than 15 siblings")
    output2.append(children)
    FAM_TABLE.add_row(output2)

print("\nFamilies")
print(FAM_TABLE)
with open('Tables.txt', 'w') as w:
    w.write(str("Individuals\n"))
    w.write(str(INDI_TABLE))
    w.write(str("\n"))
    w.write(str("Families\n"))
    w.write(str(FAM_TABLE))
