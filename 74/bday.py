import calendar
from datetime import date


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    d = date.weekday()
    if d == 0:
        return 'Monday'
    elif d == 1:
        return 'Tuesday'
    elif d == 2:
        return 'Wednesday'
    elif d == 3:
        return 'Thursday'
    elif d == 4:
        return 'Friday'
    elif d == 5:
        return 'Saturday'
    else:
        return 'Sunday'
