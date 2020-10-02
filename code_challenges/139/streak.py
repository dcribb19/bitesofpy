from datetime import datetime, timedelta, date
import re

TODAY = date(2018, 11, 12)


def extract_dates(data):
    """Extract unique dates from DB table representation as shown in Bite"""
    dates = re.findall(r'\d{4}-\d{2}-\d{2}', data)
    dates = [datetime.strptime(d, '%Y-%m-%d').date() for d in dates]
    return sorted(set(dates), reverse=True)


def calculate_streak(dates):
    """Receives sequence (set) of dates and returns number of days
       on coding streak.

       Note that a coding streak is defined as consecutive days coded
       since yesterday, because today is not over yet, however if today
       was coded, it counts too of course.

       So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
       the table makes for a 3 days coding streak.

       See the tests for more examples that will be used to pass your code.
    """
    streak = 0

    if TODAY in dates:
        streak += 1
    if TODAY - timedelta(days=1) in dates:
        streak += 1

    for d in dates:
        if d == TODAY:
            continue
        if d == TODAY - timedelta(days=1):
            if d - timedelta(days=1) in dates:
                streak += 1
        elif TODAY - timedelta(days=1) not in dates:
            break
        elif d - timedelta(days=1) in dates:
            streak += 1
        else:
            break
    return streak
