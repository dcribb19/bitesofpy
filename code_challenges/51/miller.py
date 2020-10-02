from datetime import datetime, timedelta

# https://pythonclock.org/
PY2_DEATH_DT = datetime(year=2020, month=1, day=1)
BITE_CREATED_DT = datetime.strptime('2018-02-26 23:24:04', '%Y-%m-%d %H:%M:%S')


def py2_earth_hours_left(start_date=BITE_CREATED_DT):
    """Return how many hours, rounded to 2 decimals, Python 2 has
       left on Planet Earth (calculated from start_date)"""
    time_left = PY2_DEATH_DT - start_date
    # add days and seconds to get hours
    return round(time_left.days * 24 + time_left.seconds / 3600, 2)


def py2_miller_min_left(start_date=BITE_CREATED_DT):
    """Return how many minutes, rounded to 2 decimals, Python 2 has
       left on Planet Miller (calculated from start_date)"""
    # 1 hour on Planet Miller == 7 Earth years
    # convert 1 hr and 7 years to seconds
    # convert time_left to seconds
    # set up proportion
    # divide seconds to get minutes
    miller_seconds = 3600
    earth_seconds = (timedelta(days=365) * 7).total_seconds()
    time_left = (PY2_DEATH_DT - start_date).total_seconds()
    return round(((miller_seconds * time_left) / earth_seconds) / 60, 2)
