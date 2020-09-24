from functools import wraps

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwds):
        return func(*args, **kwds)
    return wrapper


@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    if user in loggedin_users:
        return f'welcome back {user}'
    elif user in known_users:
        return 'please login'
    else:
        return 'please create an account'
