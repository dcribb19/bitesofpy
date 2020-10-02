from datetime import datetime
from datetime import timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)

today = datetime.today()
date_range_days = today.toordinal()+1 - PYBITES_BORN.toordinal()
time_delta_year = timedelta(days=365)
time_delta_hundred_days = timedelta(days=100)
special_pybites_dates = []

def gen_special_pybites_dates():
    year_date = PYBITES_BORN
    hundred_date = PYBITES_BORN
    for d in range(1, date_range_days):
        if d%100 == 0:
            hundred_date += time_delta_hundred_days
            special_pybites_dates.append(hundred_date)
        if d%365 == 0:
            year_date += time_delta_year
            special_pybites_dates.append(year_date)
    return special_pybites_dates

"""
MUCH EASIER
days = 0
while True:
    days += 1
    if days % 100 == 0 or days % 365 == 0:
        yield PYBITES_BORN + timedelta(days=days)
"""