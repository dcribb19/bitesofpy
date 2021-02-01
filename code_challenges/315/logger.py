import logging
from typing import List  # python 3.9 we can drop this


logger = logging.getLogger('app')


def sum_even_numbers(numbers: List[float]) -> float:
    """
    1. Of the numbers passed in sum the even ones
       and return the result.
    2. If all goes well log an INFO message:
       Input: {numbers} -> output: {ret}
    3. If bad inputs are passed in
       (e.g. one of the numbers is a str), catch
       the exception log it, then reraise it.
    """
    even_nums = []
    try:
        even_nums = [num for num in numbers if num % 2 == 0]
    except TypeError:
        logger.exception(f'Bad inputs: {numbers}')
        raise TypeError

    sum_even_nums = sum(even_nums)
    msg = f'Input: {numbers} -> output: {sum_even_nums}'
    logger.log(logging.INFO, msg)
    return sum_even_nums
