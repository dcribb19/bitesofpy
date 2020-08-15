from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = requests.get(PACKT).text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, 'html.parser')
    book = Book(title=soup.find(id='deal-of-the-day').h2.string.strip('</h2>\n\t'),
                description=soup.find(id='deal-of-the-day').div.div.contents[3].contents[7].string.strip(),
                image=soup.find(id='deal-of-the-day').a.img.attrs['src'],
                link=soup.find(id='deal-of-the-day').a.attrs['href'])
    return book
