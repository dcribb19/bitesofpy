import string
import re

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())


def validate_password(password):
    if len(password) < 6 or len(password) > 12:
        return False
    elif password in used_passwords:
        return False
    elif (re.search(r'[0-9]', password) and
          len(re.findall(r'[a-z]', password)) >= 2 and
          re.search(r'[A-Z]', password)):
        for char in password:
            if char in PUNCTUATION_CHARS:
                used_passwords.add(password)
                return True
    else:
        return False
