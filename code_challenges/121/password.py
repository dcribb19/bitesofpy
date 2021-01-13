from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def password_complexity(password: str) -> int:
    """Input: password string, calculate score according to 5 criteria in bite,
       return: score int"""
    score = 0
    # both upper and lower case letters
    if (any(char in ascii_lowercase for char in password) and
            any(char in ascii_uppercase for char in password)):
        score += 1
    # 1+ numbers and char
    if (any(char in digits for char in password) and
            any(char in ascii_lowercase + ascii_uppercase + punctuation
                for char in password)):
        score += 1
    # 1+ special char(s)
    if any(char in punctuation for char in password):
        score += 1
    # >= 8 chars
    if len(password) >= 8:
        score += 1
    # no repeats in 1st 8 chars
        first = password[0]
        repeat = False
        for char in password[1:]:
            if char == first:
                repeat = True
            first = char
        if not repeat:
            score += 1
    return score
