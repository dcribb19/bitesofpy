import pytz

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """
    Receive a utc datetime and one or more timezones and check if
    they are all within schedule (MEETING_HOURS)
    """
    utc_tz = pytz.timezone('UTC')
    utc = utc_tz.localize(utc)
    hours = []
    for tz in timezones:
        if tz not in TIMEZONES:
            raise ValueError
        else:
            local_time = utc.astimezone(pytz.timezone(tz)).hour
            hours.append(local_time)
    if all(hour in MEETING_HOURS for hour in hours):
        return True
    return False
