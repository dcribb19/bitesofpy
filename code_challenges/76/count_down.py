from functools import singledispatch

TYPES = [int, str, list, tuple, set, dict]


@singledispatch
def count_down(data_type):
    # TODO: Learn how to use singledispatch!
    if data_type not in TYPES:
        raise ValueError
    print(data_type)


@count_down.register(str)
def str_type(arg):
    while len(arg) != 0:
        print(arg)
        arg = arg[:-1]


@count_down.register(float)
@count_down.register(int)
def numbers(arg):
    str_type(str(arg))


@count_down.register(list)
@count_down.register(tuple)
@count_down.register(set)
def lts_type(arg):
    str_arg = ''.join([str(x) for x in arg])
    str_type(str_arg)


@count_down.register(dict)
def dict_type(arg):
    str_arg = ''.join([str(x) for x in list(arg.keys())])
    str_type(str_arg)


@count_down.register(range)
def range_type(arg):
    lts_type(list(arg))
