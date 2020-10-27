
# Implemented in order to improve code legibility
# Improve optimaztion of code
import datetime


# Format (DDMMMYYYY)
def large_age_diff(husb_date, wife_date, wedding_date):
    MONTHS = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]

    #Years
    husb_year = int(husb_date[len(husb_date)-4:])
    wife_year = int(wife_date[len(wife_date)-4:])
    wedding_year = int(wedding_date[len(wedding_date)-4:])

    #Months
    husb_month = int(MONTHS.index(husb_date[len(husb_date)-7:len(husb_date)-4])) if int(MONTHS.index(husb_date[len(husb_date)-7:len(husb_date)-4])) > 0 else 1
    wife_month = int(MONTHS.index(wife_date[len(wife_date)-7:len(wife_date)-4])) if int(MONTHS.index(wife_date[len(wife_date)-7:len(wife_date)-4])) > 0 else 1
    wedding_month = int(MONTHS.index(wedding_date[len(wedding_date)-7:len(wedding_date)-4])) if int(MONTHS.index(wedding_date[len(wedding_date)-7:len(wedding_date)-4])) > 0 else 1

    #Days
    husb_day = int(husb_date[:len(husb_date)-7])
    wife_day = int(wife_date[:len(wife_date)-7])
    wedding_day = int(wedding_date[:len(wedding_date)-7])
    
    husb_age = datetime.datetime.now() - datetime.datetime(husb_year, husb_month, husb_day)
    wife_age = datetime.datetime.now() - datetime.datetime(wife_year, wife_month, wife_day)
    wedding_ann = datetime.datetime.now() - datetime.datetime(wedding_year, wedding_month, wedding_day)
    
    if wedding_ann > husb_age or wedding_ann > wife_age:
        return False
    
    husb_wedage = husb_age - wedding_ann
    wife_wedage = wife_age - wedding_ann
    
    return (husb_wedage > 2*wife_wedage or wife_wedage > 2*husb_wedage)

large_age_diff("10MAR1890","10MAR1890", "22JUN2010")
large_age_diff("10MAR2000","27AUG2000", "22JUN1000")
large_age_diff("10MAR2000","27AUG2000", "22JUN3000")
large_age_diff("10MAR1890","27AUG1990", "22JUN2010")
large_age_diff("10MAR1990","27AUG1890", "22JUN2010")

