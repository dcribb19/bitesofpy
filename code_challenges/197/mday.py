from datetime import date
from dateutil.rrule import rrule, MONTHLY, SU


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    return list(
       rrule(MONTHLY,
             dtstart=date(year, 5, 1),
             count=1,
             byweekday=SU(2)
             )
       )[0].date()
