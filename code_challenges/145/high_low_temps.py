from collections import namedtuple
from datetime import datetime

import pandas as pd

DATA_FILE = "https://bites-data.s3.us-east-2.amazonaws.com/weather-ann-arbor.csv"
STATION = namedtuple("Station", "ID Date Value")

# 1. Create Dataframe
df = pd.read_csv(DATA_FILE)

# 2.
# Remove Leap Days between min and max df dates (2005-01-01 to 2015-12-31)
df = df[(df['Date'] != '2012-02-29') & (df['Date'] != '2008-02-29')]

# Highs/Lows for 2015
df_2015 = df[df['Date'] >= '2015-01-01']
# Highs/Lows 2005-2014
# df_04_15 = df[df['Date'] < '2015-01-01']


def high_low_record_breakers_for_2015():
    """Extract the high and low record breaking temperatures for 2015

    The expected value will be a tuple with the highest and lowest record
    breaking temperatures for 2015 as compared to the temperature data
    provided.

    NOTE:
    The date values should not have any timestamps, should be a
    datetime.date() object. The temperatures in the dataset are in tenths
    of degrees Celsius, so you must divide them by 10

    Possible way to tackle this challenge:

    1. Create a DataFrame from the DATA_FILE dataset.

    2. Manipulate the data to extract the following:
       * Extract highest temperatures for each day / station pair between 2005-2015
       * Extract lowest temperatures for each  day / station  between 2005-2015
       * Remove February 29th from the dataset to work with only 365 days

    3. Separate data into two separate DataFrames:
       * high/low temperatures between 2005-2014
       * high/low temperatures for 2015

    4. Iterate over the 2005-2014 data and compare to the 2015 data:
       * For any temperature that is higher/lower in 2015 extract ID,
         Date, Value

    5. From the record breakers in 2015, extract the high/low of all the
       temperatures
       * Return those as STATION namedtuples, (high_2015, low_2015)
    """
    max_2015 = df_2015.sort_values('Data_Value', ascending=False).iloc[0]
    min_2015 = df_2015.sort_values('Data_Value').iloc[0]
    high_2015 = STATION(
       ID=max_2015['ID'],
       Date=datetime.strptime(max_2015['Date'], '%Y-%m-%d').date(),
       Value=max_2015['Data_Value'] / 10
       )
    low_2015 = STATION(
       ID=min_2015['ID'],
       Date=datetime.strptime(min_2015['Date'], '%Y-%m-%d').date(),
       Value=min_2015['Data_Value'] / 10
       )
    return (high_2015, low_2015)
