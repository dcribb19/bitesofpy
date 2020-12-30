import hashlib

GRAVATAR_URL = ("https://www.gravatar.com/avatar/"
                "{hashed_email}?s={size}&r=g&d=robohash")


def create_gravatar_url(email: str, size: int = 200):
    """Use GRAVATAR_URL above to create a gravatar URL.

       You need to create a hash of the email passed in.

       PHP example: https://en.gravatar.com/site/implement/hash/

       For Python check hashlib check out (md5 / hexdigest):
       https://docs.python.org/3/library/hashlib.html#hashlib.hash.hexdigest
    """
    email = email.strip().lower()
    email = str.encode(email)  # convert to str to bytes
    h = hashlib.md5()
    h.update(email)
    return GRAVATAR_URL.format(hashed_email=h.hexdigest(), size=size)
