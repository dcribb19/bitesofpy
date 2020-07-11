from datetime import date, timedelta

def tomorrow():
    return date.today() + timedelta(days=1)