
# Format DD/MON/YEAR
def birth_before_marrige(birth,parent_marrige):
    MONTHS = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
    child_year = int(birth[len(birth)-4:])
    marrige_year = int(parent_marrige[len(birth)-4:])
    if marrige_year - child_year < 0:
        return True
    elif marrige_year - child_year == 0:
        child_month = int(MONTHS.index(birth[len(birth)-7:len(birth)-4]))
        marrige_month = int(MONTHS.index(parent_marrige[len(parent_marrige)-7:len(parent_marrige)-4]))
        if marrige_month - child_month < 0:
            return True
        elif marrige_month - child_month == 0:
            child_day = int(birth[:len(birth)-7])
            marrige_day = int(parent_marrige[:len(birth)-7])
            if marrige_day - child_day < 0:
                return True
    else:
        return False
        

    


