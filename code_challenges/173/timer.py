from datetime import datetime, timedelta
import re

NOW = datetime(year=2019, month=2, day=6,
               hour=22, minute=0, second=0)


def add_todo(delay_time: str, task: str,
             start_time: datetime = NOW) -> str:
    """
    Add a todo list item in the future with a delay time.

    Parse out the time unit from the passed in delay_time str:
    - 30d = 30 days
    - 1h 10m = 1 hour and 10 min
    - 5m 3s = 5 min and 3 seconds
    - 45 or 45s = 45 seconds

    Return the task and planned time which is calculated from
    provided start_time (here default = NOW):
    >>> add_todo("1h 10m", "Wash my car")
    >>> "Wash my car @ 2019-02-06 23:10:00"
    """
    days, hours, minutes, seconds = 0, 0, 0, 0
    parse_time = re.findall(r'\d+\w', delay_time)

    try:
        parse_time = [(int(re.findall(r'\d+', t)[0]),
                      re.findall(r'[a-z]', t)[0])
                      for t in parse_time
                      ]

        for time in parse_time:
            if time[1] == 'd':
                days = time[0]
            elif time[1] == 'h':
                hours = time[0]
            elif time[1] == 'm':
                minutes = time[0]
            elif time[1] == 's':
                seconds = time[0]
            else:
                seconds = time[0]
    except IndexError:
        seconds = int(parse_time[0])

    delta = timedelta(days=days,
                      hours=hours,
                      minutes=minutes,
                      seconds=seconds
                      )
    remind_time = start_time + delta
    remind_time = remind_time.strftime('%Y-%m-%d %H:%M:%S')

    return f'{task} @ {remind_time}'
