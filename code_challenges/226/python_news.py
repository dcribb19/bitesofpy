from collections import namedtuple

from bs4 import BeautifulSoup
import requests

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
URL_1 = 'https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html'
URL_2 = 'https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html'

Entry = namedtuple('Entry', 'title points comments')


def _create_soup_obj(url):
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    return BeautifulSoup(resp.text, "html.parser")


def get_top_titles(url, top=5):
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    # Make the soup!
    soup = _create_soup_obj(url)
    # Find titles.
    titles = soup.find_all('span', class_='title')
    # Get text for each title.
    titles = [title.get_text().strip() for title in titles]
    # Both points and comments are found in controls.
    controls = soup.find_all('span', class_='controls')
    # Get points.
    points = [int(item.get_text().strip().split()[0]) for item in controls]
    # Get comments.
    comments = [int(item.find_all('a')[1].get_text().split()[0])
                for item in controls]
    # Zip it all up!
    zipper = zip(titles, points, comments)
    # Create namedtuples.
    entries = [Entry(article[0], article[1], article[2]) for article in zipper]
    # Sort by highest total of points + comments and return.
    return sorted(
        entries,
        key=lambda x: x.points + x.comments,
        reverse=True
        )[:top]
