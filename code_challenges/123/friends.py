from collections import Counter, defaultdict

names = 'bob julian tim martin rod sara joyce nick beverly kevin'.split()
ids = range(len(names))
users = dict(zip(ids, names))  # 0: bob, 1: julian, etc

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
               (3, 4), (4, 5), (5, 6), (5, 7), (5, 9),
               (6, 8), (7, 8), (8, 9)]


def get_friend_with_most_friends(friendships, users=users):
    """Receives the friendships list of user ID pairs,
       parse it to see who has most friends, return a tuple
       of (name_friend_with_most_friends, his_or_her_friends)"""
    friends = _parse_friendships(friendships, users)
    friend_count = _count_friends(friends)
    # Get name of person with most friends.
    most_friends = friend_count.most_common(1)[0][0]
    return (users[most_friends], friends[most_friends])


def _parse_friendships(friendships, users):
    '''Parse friendships into a dict of keys=id, values=list of names'''
    friends = defaultdict(list)
    for k, v in friendships:
        # friendships are reciprocal!
        friends[k].append(users[v])
        friends[v].append(users[k])
    return friends


def _count_friends(friends: dict):
    '''Return friend count'''
    c = Counter()
    for k, v in friends.items():
        c[k] += len(v)
    return c
