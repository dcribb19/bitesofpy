from datetime import date, timedelta

TODAY = date.today()


def gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY):
    ret_date = start_date
    while True:
        for _ in range(num_bites):
            yield ret_date + timedelta(days=num_days)
        ret_date += timedelta(days=num_days)
