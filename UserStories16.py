def retrieveInfo():
    allMaleLastNames = []
    with open("Tables.txt") as table:
        lines = table.readlines()
        end = lines.index("Families\n") - 1
        for x in range(4, end):
            gender = lines[x].split("|")[3].replace(" ","")
            lastName = lines[x].split("|")[2].replace(" ", "").replace("/", " ").split()[1]
            if gender == "M":
                allMaleLastNames.append(lastName)
        return allMaleLastNames

allMaleLastNames = ['Diaz', 'Diaz', 'Diaz', 'Geronimo', 'Geronimo', 'Diaz', 'Pena', 'Pena', 'Pena', 'Diaz', 'Severino', 'Alayon', 'Alayon', 'Alayon', 'Alayon']

def checkMaleLastNames(lastNames):
    if not isinstance(lastNames, list):
        return False
    if lastNames == []:
        return False
    else:
        return lastNames
