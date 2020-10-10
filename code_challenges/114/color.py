import os
import sys
import urllib.request
from string import hexdigits
from textwrap import wrap

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, 'color_values.py')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/color_values.py',
    color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """
    Color class.
    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.color = color
        if color.upper() in COLOR_NAMES:
            self.rgb = COLOR_NAMES[color.upper()]
        else:
            self.rgb = None

    @staticmethod
    def hex2rgb(hex):
        """Class method that converts a hex value into an rgb one"""
        hex = hex.replace('#', '')
        if not all(x in hexdigits for x in hex) or len(hex) != 6:
            raise ValueError
        return tuple([int(x, 16) for x in wrap(hex, 2)])

    @staticmethod
    def rgb2hex(rgb):
        """Class method that converts an rgb value into a hex one"""
        hex_conversion = '#'
        for color in rgb:
            if color not in range(0, 256):
                raise ValueError
            else:
                color = f'{color:x}'
                if len(color) == 1:
                    color = '0' + color
            hex_conversion += color
        return hex_conversion

    def __repr__(self):
        """Returns the repl of the object"""
        return f"Color('{self.color}')"

    def __str__(self):
        """Returns the string value of the color object"""
        if self.rgb is None:
            return 'Unknown'
        else:
            return str(self.rgb)
