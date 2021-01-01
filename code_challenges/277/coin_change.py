from typing import List


def make_changes(n: int, coins: List[int]) -> int:
    """
    Input: n - the changes amount
          coins - the coin denominations
    Output: how many ways to make this changes
    """
    m = len(coins)
    return count(n, coins, m)


def count(n: int, coins: List[int], m: int) -> int:
    # If n == 0 then there is 1 solution (No coins used)
    if n == 0:
        return 1
    # If n < 0 then no solution exists (No negative coins exist)
    if n < 0:
        return 0
    # If there are no coins and n > 0, then no solution exists
    # No coins can be used to make change.
    if m <= 0 and n >= 1:
        return 0
    # count is sum of solutions
    # (i) including coins[m - 1] (ii) excluding coins[m - 1]
    return count(n, coins, m - 1) + count(n - coins[m - 1], coins, m)
