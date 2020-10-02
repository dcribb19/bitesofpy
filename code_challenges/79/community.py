import csv
import requests
from collections import Counter

CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'


def get_csv():
    """
    Use requests to download the csv and return the decoded content.
    """
    with requests.Session() as s:
        response = s.get(CSV_URL)
        content = response.content.decode('utf-8')

    return content


def create_user_bar_chart(content):
    """
    Receives csv file (decoded) content and print a table of timezones
    and their corresponding member counts in pluses to standard output
    """
    csv_reader = csv.reader(content.splitlines())
    # get headers
    headers = next(csv_reader)
    cnt = Counter()
    for row in csv_reader:
        cnt[row[2]] += 1
    timezones = dict(cnt)
    for key, value in sorted(timezones.items()):
        print(f'{key:<21}| {value * "+"}')
