from dateutil.rrule import rrule, DAILY


def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    max_date = max(dates)
    min_date = min(dates)
    all_dates = rrule(freq=DAILY, dtstart=min_date, until=max_date)
    return [x.date() for x in all_dates if x.date() not in dates]
