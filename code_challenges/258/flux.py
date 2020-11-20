import numpy as np
import pandas as pd

XYZ = "https://bites-data.s3.us-east-2.amazonaws.com/xyz.csv"
THRESHOLDS = (5000, 0.05)


def calculate_flux(XYZ: str = XYZ) -> list:
    """Read the data in from xyz.csv
    add two new columns, one to calculate dollar flux,
    and the other to calculate percentage flux
    return as a list of tuples
    """
    df = pd.read_csv(XYZ, dtype={'Account': str,
                                 '12/31/20': np.int32,
                                 '12/31/19': np.int32
                                 }
                     )
    df['dollar_flux'] = df['12/31/20'] - df['12/31/19']
    df['p_flux'] = df['dollar_flux'] / df['12/31/19']
    return [row[1] for row in df.iterrows()]


def identify_flux(xyz: list = calculate_flux()) -> list:
    """Load the list of tuples, iterate through
    each item and determine if it is above both
    thresholds. if so, add to the list
    """
    flagged_lines = []
    for item in xyz:
        if (abs(item.dollar_flux) > THRESHOLDS[0] and
               (abs(item.p_flux) > THRESHOLDS[1] or item.p_flux == 0)):
            flagged_lines.append(item)
    return flagged_lines
