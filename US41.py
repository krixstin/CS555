
# Format (DDMMMYYYY)
def partialDates(unkownDate):
    MONTHS = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]

    if len(unkownDate) > 9:
        return False
        
    #Years
    date_year = int(unkownDate[len(unkownDate)-4:])
    
    if len(unkownDate) == len(str(date_year)):
        return True

    #Months
    date_month = int(MONTHS.index(unkownDate[len(unkownDate)-7:len(unkownDate)-4])) if int(MONTHS.index(unkownDate[len(unkownDate)-7:len(unkownDate)-4])) > 0 else 1
    
    if len(unkownDate) == (len(str(date_year)) + len(str(MONTHS[date_month]))):
        return True

    #Days
    date_day = int(unkownDate[:len(unkownDate)-7])
    
    return 9 >= (len(str(date_year)) + len(str(MONTHS[date_month])) + len(str(date_day)))


