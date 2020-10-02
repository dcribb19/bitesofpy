import math

def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) ronud up, else round down.
       Return a new list of rounded values
    """
    if up == True:
       return [math.ceil(x) for x in transactions]
    if up == False:
       return [math.floor(x) for x in transactions]