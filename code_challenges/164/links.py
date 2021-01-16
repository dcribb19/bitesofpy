import sys

INTERNAL_LINKS = ('pybit.es', 'codechalleng.es')


def make_html_links():
    for line in sys.stdin.readlines():
        if 'http' not in line:
            continue
        href, name = line.split(',')
        href = href.strip()
        name = name.strip()
        if any(link in href for link in INTERNAL_LINKS):
            print(f'<a href="{href}">{name}</a>')
        else:
            print(f'<a href="{href}" target="_blank">{name}</a>')


if __name__ == '__main__':
    make_html_links()
