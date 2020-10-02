from collections import namedtuple

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)

# define exception classes here
class UserDoesNotExist(Exception):
    """Exception raised if user not in USERS"""


class UserAccessExpired(Exception):
    """Exception raised if expired = True"""


class UserNoPermission(Exception):
    """Exception raised if role != ADMIN"""


def get_user(username):
    for user in USERS:
        if username == user.name:
            return user


def get_secret_token(username):
    usernames = [user.name for user in USERS]
    if username not in usernames:
        raise UserDoesNotExist
    username = get_user(username)
    if username.expired == True:
        raise UserAccessExpired
    elif username.role != ADMIN:
        raise UserNoPermission
    else:
        return SECRET
