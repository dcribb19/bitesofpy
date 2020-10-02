import requests
from collections import Counter

STOCK_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()

# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    if cap == 'n/a':
        return 0
    cap = cap.lstrip('$')
    if cap.endswith('M'):
        cap = cap.rstrip('M')
        return float(cap)
    elif cap.endswith('B'):
        cap = cap.rstrip('B')
        return float(cap) * 1000


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    cap_sum = 0
    for stock in data:
        if stock['industry'] == industry:
            cap = _cap_str_to_mln_float(stock['cap'])
            cap_sum += cap
    return round(cap_sum, 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    caps = [(stock['symbol'], _cap_str_to_mln_float(stock['cap'])) for stock in data]
    return sorted(caps, key=lambda x: x[1], reverse=True)[0][0]


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    sectors = (stock['sector'] for stock in data if stock['sector'] != 'n/a')
    count = Counter(sectors).most_common()
    return (count[0][0], count[-1][0])
