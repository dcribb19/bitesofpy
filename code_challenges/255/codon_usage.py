import os
from urllib.request import urlretrieve
from collections import Counter
from itertools import product
from textwrap import wrap

# Translation Table:
# https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi#SG11
# Each column represents one entry. Codon = {Base1}{Base2}{Base3}
# All Base 'T's need to be converted to 'U's to convert DNA to RNA
TRANSL_TABLE_11 = """
    AAs  = FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = ---M------**--*----M------------MMMM---------------M------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
"""

# Converted from http://ftp.ncbi.nlm.nih.gov/genomes/archive/old_refseq/Bacteria/Staphylococcus_aureus_Newman_uid58839/NC_009641.ffn  # noqa E501
URL = "https://bites-data.s3.us-east-2.amazonaws.com/NC_009641.txt"

# Order of bases in the table
BASE_ORDER = ["U", "C", "A", "G"]


def _preload_sequences(url=URL):
    """
    Provided helper function
    Returns coding sequences, one sequence each line
    """
    filename = os.path.join(os.getenv("TMP", "/tmp"), "NC_009641.txt")
    if not os.path.isfile(filename):
        urlretrieve(url, filename)
    with open(filename, "r") as f:
        return f.readlines()


def return_codon_usage_table(
    sequences=_preload_sequences(), translation_table_str=TRANSL_TABLE_11
):
    """
    Receives a list of gene sequences and a translation table string
    Returns a string with all bases and their frequencies in a table
    with the following fields:
    codon_triplet: amino_acid_letter frequency_per_1000 absolute_occurrences

    Skip invalid coding sequences:
       --> must consist entirely of codons (3-base triplet)
    """
    codons = [''.join(x) for x in product(''.join(BASE_ORDER), repeat=3)]
    aas = TRANSL_TABLE_11.splitlines()[1].strip().replace('AAs  = ', '')
    c = Counter()
    for seq in sequences:
        c.update(wrap(seq, 3))
    freq = [round(c[codon] / sum(c.values()) * 1000, 1) for codon in codons]
    data = list(zip(codons, aas, freq, [c[codon] for codon in codons]))

    header = f'|{"  Codon AA  Freq  Count  |" * 4}\n'
    dashes = '-' * 105 + '\n'
    return_string = header + dashes

    for x in range(0, 64, 16):
        for y in range(x, x + 4):
            return_string += (f'|{data[y][0]:>5}:  {data[y][1]}   {data[y][2]:>4}  {data[y][3]:>5}  |'
                              f'{data[y + 4][0]:>5}:  {data[y + 4][1]}   {data[y + 4][2]:>4}  {data[y + 4][3]:>5}  |'
                              f'{data[y + 8][0]:>5}:  {data[y + 8][1]}   {data[y + 8][2]:>4}  {data[y + 8][3]:>5}  |'
                              f'{data[y + 12][0]:>5}:  {data[y + 12][1]}   {data[y + 12][2]:>4}  {data[y + 12][3]:>5}  |\n')
        return_string += dashes
    return return_string


if __name__ == "__main__":
    print(return_codon_usage_table())
