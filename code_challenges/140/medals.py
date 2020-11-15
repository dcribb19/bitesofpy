import pandas as pd

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"
GENDERS = ['Men', 'Women']


def athletes_most_medals(data=data):
    df = pd.read_csv(data)
    athletes = {}

    for gender in GENDERS:
        athlete = df.query(f'Gender == "{gender}"').groupby(
            'Athlete', as_index=False)['Medal'].count().sort_values(
                by='Medal', ascending=False).iloc[0]
        athletes[athlete.Athlete] = athlete.Medal

    return athletes
