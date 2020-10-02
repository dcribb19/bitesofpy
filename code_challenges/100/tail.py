def tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
    last_lines = []
    with open(filepath, 'rb') as binary_file:
        data = binary_file.readlines()
        for line in data:
           line = line.decode('utf-8')
           line = line.strip('\n')
           last_lines.append(line)
    return last_lines[-n:]
