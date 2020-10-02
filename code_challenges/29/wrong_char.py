import re

def get_index_different_char(chars):
    an_results = []
    non_an_results = []

    for char in range(len(chars)):
        check = str(chars[char])
        alpha_num_result = re.search(r'\w', check)
        non_alpha_num_result = re.search(r'\W', check)

        if alpha_num_result:
            an_results.append(chars[char])
        if non_alpha_num_result:
            non_an_results.append(chars[char])
    
    enumerate(chars)
    if len(an_results) == 1:
        return chars.index(an_results[0])
    if len(non_an_results) == 1:
        return chars.index(non_an_results[0])