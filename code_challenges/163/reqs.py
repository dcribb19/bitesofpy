from collections import defaultdict


def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    req_dict = defaultdict(dict)
    newer = []

    old_reqs = _split_reqs(old_reqs)
    new_reqs = _split_reqs(new_reqs)

    old_reqs = _convert_reqs(old_reqs)
    new_reqs = _convert_reqs(new_reqs)

    req_dict = _add_reqs_to_dict(old_reqs + new_reqs)

    # Check version numbers.
    for k in req_dict.keys():
        for x in range(len(req_dict[k][0])):
            if req_dict[k][0][x] > req_dict[k][1][x]:
                break
            elif req_dict[k][0][x] < req_dict[k][1][x]:
                newer.append(k)
                break

    return newer


def _split_reqs(reqs: str) -> list:
    '''
    Split reqs on '==' and return list of lists.
    Inner lists are [req, version].
    '''
    # Remove empty 1st line.
    reqs = reqs.splitlines()[1:]
    reqs = [req.split('==') for req in reqs]
    return reqs


def _convert_reqs(reqs: list) -> list:
    '''Convert version number into list of ints.
    Ex. '0.12.1' -> [0, 12, 1]
    '''
    for req in reqs:
        req[1] = [int(x) for x in req[1].split('.')]
    return reqs


def _add_reqs_to_dict(reqs: list) -> dict:
    '''Create a dict with req as key and
    old and new req versions as list of lists [old, new] in values.'''
    req_dict = defaultdict(list)

    for k, v in reqs:
        req_dict[k].append(v)

    return req_dict
