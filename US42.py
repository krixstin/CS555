import datetime
from datetime import timedelta

valid_dates = {
    "JAN": 30,
    "FEB": [28, 29],
    "MAR": 31,
    "APR": 30,
    "MAY": 31,
    "JUN": 30,
    "JUL": 31,
    "AUG": 31,
    "SEP": 30,
    "OCT": 31,
    "NOV": 30,
    "DEC": 31
}

def illegitimate_dates(date_string):
    date = int(date_string[0:2])
    month = date_string[2:5]
    year = int(date_string[5:])
    
    if year < 0 or year > datetime.datetime.now().year:
        return False
    elif date < 1:
        return False
    elif month not in valid_dates:
        return False
    elif month == "FEB":
        year_temp = str(year)[2:]
        if year_temp == "00":
            return (year % 100 == 0 and year % 400 == 0) and date <= valid_dates["FEB"][1]
        elif year % 4 == 0:
            return (date <= valid_dates["FEB"][1])
        else:
            return (date <= valid_dates["FEB"][0])
    else:
        return (date <= valid_dates[month])
    
    
