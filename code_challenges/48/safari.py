import os
import urllib.request

TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'

urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
    SAFARI_LOGS
)


def create_chart():
    with open(SAFARI_LOGS) as f:
        data = f.readlines()
        
    # create list of dates
    dates = []
    for line in data:
        # line[:5] == 'MM-DD'
        if line[:5] not in dates:
            dates.append(line[:5])

    for date in dates:
        indices = []
        for x in range(len(data)):
            if data[x].startswith(date) and 'sending to slack channel' in data[x]:
                # x - 1 allows us to check line above data[x]
                indices.append(x - 1)
        # don't print date if no logs for date
        if len(indices) != 0:
            print(date, end= ' ')
            for index in indices:
                if 'Python' in data[index]:
                    print(PY_BOOK, end='')
                else:
                    print(OTHER_BOOK, end='')
            print()
                    