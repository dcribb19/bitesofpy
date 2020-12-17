from typing import Dict


def decompress(string: str, table: Dict[str, str]) -> str:
    if not string:
        return string
    if not any([char in string for char in table.keys()]):
        return string
    else:
        for char in table.keys():
            string = string.replace(char, table[char])
        return decompress(string, table)
