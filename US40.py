# US40: Include input line numbers
# Author: Kristin Kim


def line_of_code(file_name):

    file = open(file_name, "r")
    content = file.read()

    d = [content.split("\n")]
    loc = len(d[0])
    return loc


print(line_of_code("DiazJGedcomProject1.ged"))
