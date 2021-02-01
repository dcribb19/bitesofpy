import csv
from io import StringIO
import pathlib
from typing import Union


# Extracted from https://en.wikipedia.org/wiki/List_of_file_signatures
MAGIC_IMAGE_TABLE = """
"magic_bytes","text_representation","offset","extension","description"
"47 49 46 38 37 61
47 49 46 38 39 61","GIF87a
GIF89a",0,"gif","Image file encoded in the Graphics Interchange Format (GIF)"
"FF D8 FF DB
FF D8 FF E0 00 10 4A 46 49 46 00 01
FF D8 FF EE
FF D8 FF E1 ?? ?? 45 78 69 66 00 00","ÿØÿÛ
ÿØÿà..JFIF..
ÿØÿîÿØÿá..Exif..",0,"jpg
jpeg","JPEG raw or in the JFIF or Exif file format"
"89 50 4E 47 0D 0A 1A 0A",".PNG....",0,"png","Image encoded in the Portable Network Graphics format"
"49 49 2A 00 (little-endian format)
4D 4D 00 2A (big-endian format)","II*.MM.*",0,"tif
tiff","Tagged Image File Format (TIFF)"
"50 31 0A","P1.",0,"pbm","Portable bitmap"
"""  # noqa: E501


class FileNotRecognizedException(Exception):
    """
    File cannot be identified using a magic table
    """


def determine_filetype_by_magic_bytes(
    file_name: Union[str, pathlib.Path],
    lookup_table_string: str = MAGIC_IMAGE_TABLE,
) -> str:
    """
    file_name: file name with path
    lookup_table_string: a comma separated text containing a magic table

    Returns: file format based on the magic bytes
    """
    reader = csv.reader(StringIO(lookup_table_string))

    with open(file_name, 'rb') as f:
        f = f.read()

    # need at least first 6 bites for fantasy pybites format
    start_bytes = f[:6]

    hex_starts = []
    for char in start_bytes:
        # strip \x from char and uppercase if letters
        b2c = hex(char)[2:].upper()  # b2c == 'byte_to_check'
        # add leading 0 if len(b2c) == 1
        if len(b2c) == 1:
            b2c = '0' + b2c
        hex_starts.append(b2c)

    # throwaways
    next(reader)  # empty line at start of str
    next(reader)  # headers

    for row in reader:
        m_bytes, _, _, _, desc = row
        if m_bytes.startswith(' '.join(hex_starts[:2])):
            return desc
        elif m_bytes.startswith(' '.join(hex_starts[1:])):
            # check pybites fantasy format
            # pybites_format_variant_1 starts FF 01
            # pybites_format_variant_3 starts EE 01
            return desc

    raise FileNotRecognizedException

# Set up for your convenience when coding:
#  - creates a test_image.gif GIF file
#  - calls determine_filetype_by_magic_bytes
#  - prints out file type


if __name__ == "__main__":
    test_filename = "test_image.gif"
    print(f"Script invoked directly. Writing out test file {test_filename}")
    with open(test_filename, "wb") as f:
        f.write(
            b"\x47\x49\x46\x38\x37\x61\x01\x00x01\x00\x80\x00\x00\xff\xff\xff"
            b"\xff\xff\xff\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02"
            b"\x44\x01\x00\x3b"
        )
    print("Testing file format")
    print(determine_filetype_by_magic_bytes(test_filename))
