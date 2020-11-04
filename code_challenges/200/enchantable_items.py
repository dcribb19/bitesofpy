from collections import defaultdict, OrderedDict
from dataclasses import dataclass, field
from pathlib import Path
from urllib.request import urlretrieve

from bs4 import BeautifulSoup as Soup

out_dir = "/tmp"
html_file = f"{out_dir}/enchantment_list_pc.html"

HTML_FILE = Path(html_file)
# source:
# https://www.digminecraft.com/lists/enchantment_list_pc.php
URL = ("https://bites-data.s3.us-east-2.amazonaws.com/"
       "minecraft-enchantment.html")


@dataclass
class Enchantment:
    """Minecraft enchantment class
    Implements the following:
        id_name, name, max_level, description, items
    """
    id_name: str
    name: str
    max_level: int
    description: str
    items: list = field(default_factory=list)

    def __str__(self) -> str:
        return f'{self.name} ({self.max_level}): {self.description}'


@dataclass
class Item:
    """Minecraft enchantable item class
    Implements the following:
        name, enchantments
    """
    name: str
    enchantments: list = field(default_factory=list)

    def __str__(self) -> str:
        ret_string = f"{self.name.replace('_', ' ').title()}: "
        for enchantment in self.enchantments:
            ret_string += f'\n  [{enchantment.max_level}] {enchantment.id_name}'
        return ret_string.strip()


def generate_enchantments(soup):
    """Generates a dictionary of Enchantment objects
    With the key being the id_name of the enchantment.
    """
    enchantments = {}
    rows = soup.table.find_all('tr')
    # Remove header row
    rows = rows[1:]
    for row in rows:
        columns = row.find_all('td')
        id_name = columns[0].find('a').get('href').replace(
            '/enchantments/', '').replace('.php', '')

        items = columns[4].contents[0].get('data-src').split(
            'images/')[1].replace('.png', '')
        items = items.replace('enchanted_iron_', '')
        items = items.replace('enchanted_', '')
        items = items.replace('_sm', '')
        if items != 'fishing_rod':
            items = items.split('_', maxsplit=3)
        else:
            items = [items]

        enchantments[id_name] = Enchantment(
            id_name,
            name=row.find('a').text,
            max_level=_convert_roman_numeral(columns[1].text),
            description=columns[2].text,
            items=items
        )
    return enchantments


def generate_items(data):
    """Generates a dictionary of Item objects
    With the key being the item name.
    """
    item_dict = {}
    item_objs = defaultdict(list)
    for k, v in data.items():
        for item in v.items:
            item_objs[item].append(v)
    for k, v in item_objs.items():
        item_dict[k] = Item(k, v)
    # sort alphabetically by keys
    item_dict = OrderedDict(sorted(item_dict.items(), key=lambda x: x[0]))
    for k in item_dict.keys():
        item_dict[k].enchantments = sorted(
            item_dict[k].enchantments,
            key=lambda x: x.id_name
            )
    return item_dict


def get_soup(file=HTML_FILE):
    """Retrieves/takes source HTML and returns a BeautifulSoup object"""
    if isinstance(file, Path):
        if not HTML_FILE.is_file():
            urlretrieve(URL, HTML_FILE)

        with file.open() as html_source:
            soup = Soup(html_source, "html.parser")
    else:
        soup = Soup(file, "html.parser")
    return soup


def _convert_roman_numeral(numeral: str) -> int:
    NUMERALS = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5}
    return NUMERALS[numeral]


def main():
    """This function is here to help you test your final code.
    Once complete, the print out should match what's at the bottom
    of this file"""
    soup = get_soup()
    enchantment_data = generate_enchantments(soup)
    minecraft_items = generate_items(enchantment_data)
    for item in minecraft_items:
        print(minecraft_items[item], "\n")


if __name__ == "__main__":
    main()

"""
Armor:
  [1] binding_curse
  [4] blast_protection
  [4] fire_protection
  [4] projectile_protection
  [4] protection
  [3] thorns

Axe:
  [5] bane_of_arthropods
  [5] efficiency
  [3] fortune
  [5] sharpness
  [1] silk_touch
  [5] smite

Boots:
  [3] depth_strider
  [4] feather_falling
  [2] frost_walker

Bow:
  [1] flame
  [1] infinity
  [5] power
  [2] punch

Chestplate:
  [1] mending
  [3] unbreaking
  [1] vanishing_curse

Crossbow:
  [1] multishot
  [4] piercing
  [3] quick_charge

Fishing Rod:
  [3] luck_of_the_sea
  [3] lure
  [1] mending
  [3] unbreaking
  [1] vanishing_curse

Helmet:
  [1] aqua_affinity
  [3] respiration

Pickaxe:
  [5] efficiency
  [3] fortune
  [1] mending
  [1] silk_touch
  [3] unbreaking
  [1] vanishing_curse

Shovel:
  [5] efficiency
  [3] fortune
  [1] silk_touch

Sword:
  [5] bane_of_arthropods
  [2] fire_aspect
  [2] knockback
  [3] looting
  [1] mending
  [5] sharpness
  [5] smite
  [3] sweeping
  [3] unbreaking
  [1] vanishing_curse

Trident:
  [1] channeling
  [5] impaling
  [3] loyalty
  [3] riptide
"""
