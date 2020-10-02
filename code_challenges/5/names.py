NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    title_names = []
    for name in names:
        name = name.title()
        if name not in title_names:
            title_names.append(name)
    return title_names


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    # ...
    last_names = []
    surname_desc = []
    for name in names:
        last_names.append(name.split()[-1])
    for last_name in sorted(last_names, reverse=True):
        for name in names:
            if name.endswith(last_name):
                surname_desc.append(name)
    return surname_desc


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    # ...
    first_names = []
    for name in names:
        first_names.append(name.split()[0])
    short_name = first_names[0]
    for name in first_names:
        if len(name) < len(short_name):
            short_name = name
    return short_name