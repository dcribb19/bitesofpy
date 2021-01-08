from typing import Dict


def get_weekdays(calendar_output: str) -> Dict[int, str]:
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    day_dict = {}
    # month YYYY not needed (index 0)
    days = calendar_output.splitlines()[1].split()
    rows = [row.split() for row in calendar_output.splitlines()[2:]]
    # take care of potentially partial 1st row
    row_1 = [int(x) for x in rows[0]]
    row_1 = zip(row_1, days[-len(row_1):])
    for day in row_1:
        day_dict[day[0]] = day[1]
    # remaining rows
    rem_rows = rows[1:]
    for row in rem_rows:
        row = [int(day) for day in row]
        for day in zip(row, days):
            day_dict[day[0]] = day[1]

    return day_dict
