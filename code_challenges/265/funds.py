IMPOSSIBLE = 'Mission impossible. No one can contribute.'


def max_fund(village):
    """Find a contiguous subarray with the largest sum."""
    # Hint: while iterating, you could save the best_sum collected so far
    # return total, starting, ending
    total = 0
    starting = 0
    ending = 0

    if all(family < 0 for family in village):
        print(IMPOSSIBLE)
        return (total, starting, ending)

    for x in range(len(village)):
        remaining = village[x:]
        # Don't want to start with a 0 donation.
        if remaining[0] == 0:
            continue

        for family in range(len(remaining)):
            if total < sum(remaining[:family + 1]):
                total = sum(remaining[:family + 1])
                starting = x + 1
                ending = starting + family
    return (total, starting, ending)
