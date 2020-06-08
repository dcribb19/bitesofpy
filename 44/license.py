import secrets
import string

alphabet = string.ascii_uppercase + string.digits

def gen_key(parts=4, chars_per_part=8):
    x = 0
    key = ''
    while x < parts:
        key += ''.join(secrets.choice(alphabet) for i in range(chars_per_part))
        if x < parts - 1:
            key += '-'
        x += 1
    return key
    