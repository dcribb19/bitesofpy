from string import digits

VALID_IP_CHARS = digits + '.'


def extract_ipv4(data):
    """
    Given a nested list of data, return a list of IPv4 address
    information that can be extracted (ip, mask)
    """
    ipv4s = []
    data = list(_flatten(data))

    # len(data) must be at least 4 in order to have a valid ip and mask
    if len(data) < 4:
        return ipv4s

    for x in range(len(data)):
        if data[x] == 'ip':
            ip = data[x + 1]
            mask = data[x + 3]
            if ip is not None and mask is not None:
                ip = ip.replace('"', '')
                if all([char in VALID_IP_CHARS for char in ip]):
                    ipv4s.append((ip.replace('"', ''), mask))
    return ipv4s


def _flatten(data):
    '''Flatten a list of lists into one list.'''
    for item in data:
        if isinstance(item, str) or item is None:
            yield item
        else:
            yield from _flatten(item)
