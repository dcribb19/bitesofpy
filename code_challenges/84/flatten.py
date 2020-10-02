def unpack_head(head, flat_list):
    if isinstance(head, (list, tuple)):
        for item in head:
            unpack_head(item, flat_list)
    else:
        flat_list.append(head)


def flatten(list_of_lists, flat_list=[]):
    if not any([isinstance(lst, (list, tuple)) for lst in list_of_lists]):
        flattened = flat_list.copy()
        flat_list.clear()
        return flattened
    else:
        head = list_of_lists[0]
        no_head = list_of_lists[1:]
        unpack_head(head, flat_list)
        return flatten(no_head)
