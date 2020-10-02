from collections import namedtuple
from datetime import datetime
import json


blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here
Blog = namedtuple('Blog', 'name, founders, started, tags, location, site')

def dict2nt(dict_):
    return Blog._make(dict_.values())


def nt2json(nt):
    dt_convert = nt.started.strftime('%Y %m %d')
    nt = nt._replace(started=dt_convert)
    return json.JSONEncoder().encode(nt._asdict())
