from collections import Counter

import requests
import pandas as pd

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()

df = pd.DataFrame(data)

# your turn:


def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    maker_year_count = df.groupby(['year', 'automaker'])['model'].count()
    for maker in maker_year_count[year].index:
        if maker_year_count[year].get(key=maker) == maker_year_count[year].max():
            return maker


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    return {model for model in df[(df['automaker'] == automaker) & (df['year'] == year)]['model']}
