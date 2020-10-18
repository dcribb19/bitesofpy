from urllib.request import urlretrieve
from pathlib import Path

import gender_guesser.detector as gender
from bs4 import BeautifulSoup as Soup
from collections import Counter

TMP = Path('/tmp')
PYCON_HTML = TMP / "pycon2019.html"
PYCON_PAGE = ('https://bites-data.s3.us-east-2.amazonaws.com/'
              'pycon2019.html')

if not PYCON_HTML.exists():
    urlretrieve(PYCON_PAGE, PYCON_HTML)


def _get_soup(html=PYCON_HTML):
    return Soup(html.read_text(encoding="utf-8"), "html.parser")


def get_pycon_speaker_first_names(soup=_get_soup()):
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
       speakers (class "speaker"). Note that some items contain
       multiple speakers so you need to extract them.
       Return a list of first names
    """
    speakers = soup.find_all('span', class_='speaker')
    all_names = [speaker.get_text().strip() for speaker in speakers]
    for name in all_names:
        if ',' in name:
            all_names.remove(name)
            new = name.split(',')
            for n in new:
                all_names.append(n.strip())
        if '/' in name:
            all_names.remove(name)
            new = name.split('/')
            for n in new:
                all_names.append(n.strip())
    first_names = [name.split()[0] for name in all_names]
    return first_names


def get_percentage_of_female_speakers(first_names):
    """Run gender_guesser on the names returning a percentage
       of female speakers (female and mostly_female),
       rounded to 2 decimal places."""
    d = gender.Detector()
    c = Counter([d.get_gender(name) for name in first_names])
    return round((c['female'] + c['mostly_female']) / sum(c.values()) * 100, 2)


if __name__ == '__main__':
    names = get_pycon_speaker_first_names()
    perc = get_percentage_of_female_speakers(names)
    print(perc)
