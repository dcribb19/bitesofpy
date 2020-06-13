def count_indents(text: str):
    """Takes a string and counts leading white spaces, return int count"""
    space_count = 0
    for char in text:
        if text.startswith(' '):
            if char.isspace():
                space_count += 1
            else:
                break
    return space_count

