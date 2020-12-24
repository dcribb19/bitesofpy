from collections import defaultdict
from datetime import date
from typing import Dict, List, Sequence, NamedTuple


class MovieRented(NamedTuple):
    title: str
    price: int
    date: date


RentingHistory = Sequence[MovieRented]
STREAMING_COST_PER_MONTH = 12
STREAM, RENT = 'stream', 'rent'


def rent_or_stream(
    renting_history: RentingHistory,
    streaming_cost_per_month: int = STREAMING_COST_PER_MONTH
) -> Dict[str, str]:
    """Function that calculates if renting movies one by one is
       cheaper than streaming movies by months.

       Determine this PER MONTH for the movies in renting_history.

       Return a dict of:
       keys = months (YYYY-MM)
       values = 'rent' or 'stream' based on what is cheaper

       Check out the tests for examples.
    """
    monthly_rent: Dict[str, List[int]] = defaultdict(list)
    # Group rent prices by month
    for movie in renting_history:
        month = movie.date.strftime('%Y-%m')
        monthly_rent[month].append(movie.price)

    r_or_s: Dict[str, str] = {}
    for month, rent in monthly_rent.items():
        total_rent = sum(rent)
        if total_rent > streaming_cost_per_month:
            r_or_s[month] = STREAM
        else:
            r_or_s[month] = RENT
    return r_or_s
