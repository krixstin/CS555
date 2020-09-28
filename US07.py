# Get info needed to complete the test
def retrieveInfo():
    result = []
    with open("Tables.txt") as output:
        lines = output.readlines()
        end = lines.index("Families\n") - 1
        for x in range(4, end):
            ages = lines[x].split("|")[5].replace(" ","")
            result.append(ages)
        return result
        
        
def less_than_150(ages):
    if ages == []:
        return False
    for x in range(len(ages)):
        if '150' in ages:
            return False
    return True
            
