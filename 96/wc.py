def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    lines = 0
    words = 0
    chars = 0

    with open(file_) as f:
        data = f.read()
        data = data.splitlines(keepends=True)
        lines = len(data)
        
        for line in data:
            if line is None:
                continue
            words += len(line.split())
            chars += len(line)
        
    return str(lines) + '    ' + str(words) + '    ' + str(chars) + ' ' + str(file_)


if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))
