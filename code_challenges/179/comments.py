import re


def strip_comments(code: str) -> str:
    '''
    - strip all comments from code
    - going to replace all comments with ' ' and filter out with str.isspace()
      because we want to keep empty lines from original code
    '''
    # line starts or inline comments
    new_code = re.sub(r'# .*', ' ', code)

    # single line docstrings
    doc_strings = re.findall(r'""".*"""', new_code, re.MULTILINE)
    for line in doc_strings:
        if line in new_code:
            new_code = new_code.replace(line, ' ')

    # multiline docstrings
    multiline = re.findall(r'""".*"""', new_code, re.DOTALL | re.MULTILINE)
    for line in multiline:
        if line in new_code:
            new_code = new_code.replace(line, ' ')

    new_code = [line for line in new_code.splitlines()
                if not line.isspace()]

    return '\n'.join(new_code).strip()
