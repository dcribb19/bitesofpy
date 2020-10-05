# rename.py -
# Substitutes correct links to reflect /code_challenges/ folder in README.md

import re


def rename_links(input_file):
    with open(input_file, 'r+') as f:
        lines = f.read()
        f.seek(0)
        f.write(re.sub(
            r'bitesofpy/tree/master/',
            r'bitesofpy/tree/master/code_challenges/',
            lines
            )
        )
        f.truncate()
