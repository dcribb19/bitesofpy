# nice snippet: https://gist.github.com/tonybruess/9405134
from collections import namedtuple
import re
from typing import Dict, List

social_platforms = """Twitter
  Min: 1
  Max: 15
  Can contain: a-z A-Z 0-9 _

Facebook
  Min: 5
  Max: 50
  Can contain: a-z A-Z 0-9 .

Reddit
  Min: 3
  Max: 20
  Can contain: a-z A-Z 0-9 _ -
"""

# note range is of type range and regex is a re.compile object
Validator = namedtuple('Validator', 'range regex')


def _chunks(platforms: List[str], n: int):
    """Yield successive n-sized chunks from platforms"""
    for i in range(0, len(platforms), n):
        yield platforms[i:i+n]


def parse_social_platforms_string(
        platforms: str = social_platforms) -> Dict[str, Validator]:
    """Convert the social_platforms string above into a dict where
       keys = social platforms name and values = validator namedtuples"""
    platform_dict = {}
    platforms = [x.strip() for x in platforms.splitlines() if x]
    for platform in _chunks(platforms, 4):
        name, m_in, m_ax, pattern = platform
        platform_dict[name] = Validator(
            range(int(m_in.split(' ')[1]),
                  int(m_ax.split(' ')[1])),
            re.compile(f"[{pattern.split(':')[1].replace(' ', '')}]"))
    return platform_dict


def validate_username(platform: str, username: str) -> bool:
    """Receives platforms(Twitter, Facebook or Reddit) and username string,
       raise a ValueError if the wrong platform is passed in,
       return True/False if username is valid for entered platform"""
    all_validators = parse_social_platforms_string()
    if platform not in all_validators:
        raise ValueError
    val = all_validators[platform]
    if (len(username) in val.range and
            len(val.regex.findall(username)) == len(username)):
        return True
    return False
