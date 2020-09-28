
def uniqueID(id):
    unique = 0
    unique = len(set(id)) == len(id)
    if unique:
        return True
    else:
        return False

def uniqueFirstNameFam(children, individuals):
    familychild = []
    names = []
    dates = []
    name = ""
    date = ""

    for i in children:
        familychild = individuals['@'+i+'@']
        name = familychild[0]
        names.append(name.split()[0])
        date = familychild[0]
        dates.append(date.split()[0])

    uniqueN = 0
    uniqueD = 0
    uniqueN = len(set(names)) == len(names)
    uniqueD = len(set(dates)) == len(dates)
    if uniqueN and uniqueD:
        return True
    else:
        return False

