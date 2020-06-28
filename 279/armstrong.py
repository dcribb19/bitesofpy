def is_armstrong(n: int) -> bool:
    num_digits = len(str(n))
    digits = str(n)
    number = 0
    for digit in digits:
        number += int(digit) ** num_digits
    if number == n:
        return True
    else:
        return False
