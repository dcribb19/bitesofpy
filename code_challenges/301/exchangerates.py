import os
from collections import OrderedDict
from datetime import date, datetime, timedelta
import json
from pathlib import Path
from typing import Dict, List
from urllib.request import urlretrieve

URL = "https://bites-data.s3.us-east-2.amazonaws.com/exchangerates.json"
TMP = Path(os.getenv("TMP", "/tmp"))
RATES_FILE = TMP / "exchangerates.json"

if not RATES_FILE.exists():
    urlretrieve(URL, RATES_FILE)

daily_rates = json.loads(RATES_FILE.read_text())["rates"]


def get_all_days(start_date: date, end_date: date) -> List[date]:
    num_days = (end_date - start_date).days
    all_days = [start_date + timedelta(days=x) for x in range(num_days + 1)]
    return all_days


def get_base_dates(daily_rates: dict) -> List[date]:
    '''return a sorted list of date objects from list of strings'''
    return [datetime.strptime(day, '%Y-%m-%d').date() for
            day in sorted(daily_rates.keys())]


def match_daily_rates(
    start: date, end: date, daily_rates: dict
) -> Dict[date, date]:
    match_days = {}
    days = get_all_days(start, end)
    base_dates = get_base_dates(daily_rates)

    for day in days:
        if day in base_dates:
            match_days[day] = day
        else:
            new_day = day
            while new_day not in base_dates:
                new_day -= timedelta(days=1)
            match_days[day] = new_day
    return match_days


def exchange_rates(
    start_date: str = "2020-01-01", end_date: str = "2020-09-01"
) -> Dict[date, dict]:

    exchange_rates = OrderedDict()

    start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

    if start_date < datetime.strptime(
                        sorted(daily_rates.keys())[0], '%Y-%m-%d'
                        ).date():
        raise ValueError('Start date is before the start of the dataset.')
    if end_date > datetime.strptime(
                        sorted(daily_rates.keys())[-1], '%Y-%m-%d'
                        ).date():
        raise ValueError('End date is after the end of the dataset.')

    match_days = match_daily_rates(start_date, end_date, daily_rates)
    for day in sorted(match_days.keys()):
        exchange_rates[day] = {'Base Date': match_days[day],
                               'USD': daily_rates[match_days[day].strftime(
                                   '%Y-%m-%d')]['USD'],
                               'GBP': daily_rates[match_days[day].strftime(
                                   '%Y-%m-%d')]['GBP']}
    return exchange_rates
