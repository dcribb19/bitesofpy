from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup


# prep data
tmp = os.getenv("TMP", "/tmp")
page = 'us_holidays.html'
holidays_page = os.path.join(tmp, page)
urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{page}',
    holidays_page
)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """
    Receive scraped html output, make a BS object, parse the bank
    holiday table (css class = list-table), and return a dict of
    keys -> months and values -> list of bank holidays
    """
    soup = BeautifulSoup(content, 'html.parser')
    holiday_table = soup.table.tbody.find_all('tr')
    for row in holiday_table:
        # Get month from date [5:7]
        date = row.time.get_text()[5:7]
        holiday = row.a.get_text().strip()
        holidays[date].append(holiday)

    return holidays
