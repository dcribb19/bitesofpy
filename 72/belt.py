from collections import OrderedDict

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()
HONORS = zip(scores, belts)


def get_belt(user_score: int):
    if user_score < scores[0]:
        return None
    elif user_score >= scores[-1]:
        return belts[-1]
    else:
        for x in range(len(scores) - 1):
            if user_score >= scores[x] and user_score < scores[x+1]:
                return belts[x]
    