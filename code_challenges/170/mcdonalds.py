import pandas as pd

data = "https://s3.us-east-2.amazonaws.com/bites-data/menu.csv"
# load the data in once, functions will use this module object
df = pd.read_csv(data)

pd.options.mode.chained_assignment = None  # ignore warnings


def get_food_most_calories(df=df):
    """Return the food "Item" string with most calories"""
    return df.sort_values('Calories', ascending=False).iloc[0]['Item']


def get_bodybuilder_friendly_foods(df=df, excl_drinks=False):
    """Calulate the Protein/Calories ratio of foods and return the
       5 foods with the best ratio.

       This function has a excl_drinks switch which, when turned on,
       should exclude 'Coffee & Tea' and 'Beverages' from this top 5.

       You will probably need to filter out foods with 0 calories to get the
       right results.

       Return a list of the top 5 foot Item stings."""
    # Remove 0 Calorie foods.
    df = df[df['Calories'] != 0]

    if excl_drinks:
        df = df[(df['Category'] != 'Beverages') &
                (df['Category'] != 'Coffee & Tea')]

    pro_cal = df[['Item', 'Calories', 'Protein']]
    pro_cal['Pro_Cal_Ratio'] = pro_cal['Protein'] / pro_cal['Calories']

    return list(pro_cal.sort_values(
        'Pro_Cal_Ratio', ascending=False).head(5)['Item']
        )
