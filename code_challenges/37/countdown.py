def countdown_for(start=10):
    for i in reversed(range(1, start + 1)):
        print(i)
    print('time is up')


def countdown_recursive(start=10):
    # base case
    if start == 0:
        print('time is up')
    # recursive case
    else:
        print(start)
        countdown_recursive(start - 1)
