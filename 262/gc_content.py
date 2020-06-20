from collections import Counter

def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    sequence = sequence.upper()
    sc = Counter(sequence)
    return round((sc['C'] + sc['G']) / (sc['A'] + sc['C'] + sc['G'] + sc['T']) * 100, 2)
