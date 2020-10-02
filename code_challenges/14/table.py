import random

names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
aliases = 'Pythonista Nerd Coder'.split() * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = ' | '


def generate_table(*args):
    num_args = len(args)
    if num_args == 1:
        return (arg for arg in args[0])
    elif num_args == 2:
        args = list(zip(args[0], args[1]))
        return (str(args[x][0]) + SEPARATOR + str(args[x][1]) for x in range(0, len(args)))
    elif num_args == 3:
        args = list(zip(args[0], args[1], args[2]))
        return (str(args[x][0]) + SEPARATOR + str(args[x][1]) 
                + SEPARATOR + str(args[x][2]) for x in range(0, len(args)))
    else:
        args = list(zip(args[0], args[1], args[2], args[3]))
        return (str(args[x][0]) + SEPARATOR + str(args[x][1]) 
                + SEPARATOR + str(args[x][2]) + SEPARATOR + str(args[x][3]) for x in range(0, len(args)))
