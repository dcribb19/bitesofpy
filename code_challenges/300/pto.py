import calendar
from datetime import date, timedelta
from math import ceil
from typing import List


ERROR_MSG = (
    "Unambiguous value passed, please specify either start_month or show_workdays"
)
FEDERAL_HOLIDAYS = (
    date(2020, 9, 7),   # MONDAY
    date(2020, 10, 12),  # MONDAY
    date(2020, 11, 11),
    date(2020, 11, 26),
    date(2020, 12, 25),  # FRIDAY
)
WFH = (calendar.TUESDAY, calendar.WEDNESDAY)
WEEKENDS = (calendar.SATURDAY, calendar.SUNDAY)
AT_HOME = WFH + WEEKENDS


def four_day_weekends(
        *args,
        start_month: int = 8,
        paid_time_off: int = 200,
        year: int = 2020,
        show_workdays: bool = False
        ) -> None:
    """Generates four day weekend report.

    The four day weekends are calculated from the start_month through the end
    of the year along with the number of work days for the same time period.
    The reports takes into account any holidays that might fall within that
    time period and days designated as working from home (WFH).

    If show_workdays is set to True, a report with the work days is generated
    instead of the four day weekend dates.

    Args:
        start_month (int, optional): Month to start. Defaults to 8.
        paid_time_off (int, optional): Paid vacation days
        year (int, optional): Year to calculate, defaults to current year
        show_workdays (bool, optional): Enables work day report.
        Defaults to False.

    Raises:
        ValueError: ERROR_MSG
    """
    if args:
        raise ValueError(ERROR_MSG)

    date_range = _date_range(start_month, year)
    four_day_weekends, work_days = _get_four_day_weekends(date_range)
    use_or_lose = ceil(paid_time_off / 8)

    if show_workdays:
        len_wd = len(work_days)
        print(f'Remaining Work Days: {len_wd * 8} ({len_wd} days)')
        for dt in work_days:
            print(dt)
    else:
        print(f'{len(four_day_weekends)} Four-Day Weekends'.center(24))
        print('=' * 24)
        print(f'    PTO: {paid_time_off} ({int(paid_time_off / 8)} days)')
        # PTO BALANCE = PTO - (Amount of 4 day weekends * 2 days off (16 hrs))
        balance = paid_time_off - (len(four_day_weekends) * 2 * 8)
        print(f'BALANCE: {balance} ({abs(int(balance / 8))} days)\n')

        if paid_time_off % 2 != 0:
            must_take = work_days[-use_or_lose]
            star = False

            for weekend in four_day_weekends:
                # '*' LOGIC.
                if must_take < weekend[0] and star is False:
                    print(f'{weekend[0]} - {weekend[3]}*')
                    star = True
                else:
                    print(f'{weekend[0]} - {weekend[3]}')
        else:
            for weekend in four_day_weekends:
                # '*' LOGIC.
                if four_day_weekends.index(weekend) == len(four_day_weekends) - ceil(use_or_lose / 2):
                    print(f'{weekend[0]} - {weekend[3]}*')
                else:
                    print(f'{weekend[0]} - {weekend[3]}')


def _date_range(start_month: int, year: int) -> List[date]:
    '''Return a list of date objects from start month to end of year.'''
    start_date = date(year, start_month, 1)
    year_end = date(year, 12, 31)

    dates = [start_date]

    while dates[-1] < year_end:
        dates.append(dates[-1] + timedelta(days=1))

    return dates


def _get_four_day_weekends(date_range):
    '''Return a list of lists of four-day weekends through end of year.'''
    four_day_weekends = []
    workdays = []

    # IF MONDAY BEFORE 1st FRIDAY, ADD THE MONDAY.
    for dt in date_range[:7]:
        if calendar.weekday(dt.year, dt.month, dt.day) == calendar.FRIDAY:
            fri = date_range.index(dt)
            if fri >= 4:
                # fri >= 4, means a Monday does exist.
                workdays.append(date_range[fri - 4])

    for dt in date_range:
        # ALL THURSDAYS ARE WORK DAYS, except Holidays
        if (calendar.weekday(dt.year, dt.month, dt.day) == calendar.THURSDAY
                and dt not in FEDERAL_HOLIDAYS):
            workdays.append(dt)
        # IDENTIFY 4-DAY WEEKENDS THAT ARE NOT HOLIDAY WEEKENDS.
        # Start by looking at Fridays.
        elif calendar.weekday(dt.year, dt.month, dt.day) == calendar.FRIDAY:
            four_day = date_range[
                date_range.index(dt): date_range.index(dt) + 4
                ]
            # Check to see if any part of the 4-day weekend is a Holiday.
            if not any(day in FEDERAL_HOLIDAYS for day in four_day):
                four_day_weekends.append(four_day)
            # I'M NOT SURE THAT THIS IS CORRECT.
                '''
                This does not take into account Friday as a work day if the
                holiday is on Monday. It does account for Monday as a work
                day if holiday is on Friday.

                Default args with both Mondays and Fridays in Holiday weekends:
                1. Remaining workday count should be 25, not 23.
                2. With neither taken into account (Monday nor Friday),
                   remaining workdays should be 22, not 23.
                3. With only the Fridays, remaining workdays should be 24,
                   not 23.
                '''
            else:
                for day in four_day:
                    if day not in FEDERAL_HOLIDAYS and calendar.weekday(
                            day.year,
                            day.month,
                            day.day
                            ) == calendar.MONDAY:
                        workdays.append(day)

    return four_day_weekends, workdays


if __name__ == "__main__":
    four_day_weekends()
