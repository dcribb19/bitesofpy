from decimal import Decimal, ROUND_DOWN

TWO_PLACES = Decimal(10) ** -2


def check_split(item_total, tax_rate, tip, people):
    """Calculate check value and evenly split.

       :param item_total: str (e.g. '$8.68')
       :param tax_rate: str (e.g. '4.75%)
       :param tip: str (e.g. '10%')
       :param people: int (e.g. 3)

       :return: tuple of (grand_total: str, splits: list)
                e.g. ('$10.00', [3.34, 3.33, 3.33])
    """
    # Format Decimals
    item_total = Decimal(item_total.strip('$'))
    tax_rate = Decimal(tax_rate.strip('%')) * TWO_PLACES
    tip = Decimal(tip.strip('%')) * TWO_PLACES
    # Calculations
    tax_total = (item_total * tax_rate).quantize(TWO_PLACES)
    tip_total = ((item_total + tax_total) * tip).quantize(TWO_PLACES)
    grand_total = (item_total + tax_total + tip_total).quantize(TWO_PLACES)
    # Divide it up!
    split = (grand_total / people).quantize(TWO_PLACES, rounding=ROUND_DOWN)
    splits = [split for x in range(people)]
    s_splits = sum(splits)

    for x in range(len(splits)):
        if s_splits != grand_total:
            splits[x] += Decimal('0.01')
            s_splits = sum(splits)
        else:
            break

    return ('$' + str(grand_total), splits)
