from dataclasses import dataclass
from operator import attrgetter
from pathlib import Path
from urllib.request import urlretrieve

from bs4 import BeautifulSoup

url = ("https://bites-data.s3.us-east-2.amazonaws.com/"
       "best-programming-books.html")
tmp = Path("/tmp")
html_file = tmp / "books.html"

if not html_file.exists():
    urlretrieve(url, html_file)


@dataclass
class Book:
    """Book class should instatiate the following variables:

    title - as it appears on the page
    author - should be entered as lastname, firstname
    year - four digit integer year that the book was published
    rank - integer rank to be updated once the books have been sorted
    rating - float as indicated on the page
    """
    title: str
    author: str
    year: int
    rank: int
    rating: float

    def __str__(self) -> str:
        return (f'[{self.rank:03}] {self.title} ({self.year})\n'
                f'      {self.author} {float(self.rating)}')


def _get_soup(file):
    '''
    Given: return BeautifulSoup(file.read_text(), "html.parser"),
    UnicodeDecodeError: 'charmap' codec can't decode byte 0x90 in
    position 40858: character maps to <undefined>
    '''
    with open(file, encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    return soup


def display_books(books, limit=10, year=None):
    """Prints the specified books to the console

    :param books: list of all the books
    :param limit: integer that indicates how many books to return
    :param year: integer indicating the oldest year to include
    :return: None
    """
    print_count = 0
    if not year:
        for book in books:
            if print_count < limit:
                print(book)
                print_count += 1
    else:
        for book in books:
            if book.year >= year and print_count < limit:
                print(book)
                print_count += 1


def load_data():
    """Loads the data from the html file

    Creates the soup object and processes it to extract the information
    required to create the Book class objects and returns a sorted list
    of Book objects.

    Books should be sorted by rating, year, title, and then by author's
    last name. After the books have been sorted, the rank of each book
    should be updated to indicate this new sorting order.The Book object
    with the highest rating should be first and go down from there.
    """
    py_books = []
    soup = _get_soup(html_file)
    books = soup.find_all('div', class_='book accepted normal')
    for book in books:
        title = book.find('h2').text
        if 'python' in title.lower():
            author = book.find('h3', class_='authors').find('a').text.split()
            year = book.find('span', class_='date')
            rank = book.find('div', class_='rank')
            rating = book.find('span', class_='our-rating')
            if all([author, year, rank, rating]):
                if len(author) == 3:
                    first_name = author[:2]
                    first_name = ' '.join(first_name)
                    last_name = author[-1]
                    author = [last_name, first_name]
                else:
                    author.reverse()
                py_books.append(Book(
                    title,
                    ', '.join(author),
                    int(year.text.strip(' |')),
                    int(rank.text),
                    float(rating.text)
                ))

    # Sort
    py_books = sorted(py_books, key=attrgetter('author'.split(',')[0]))
    py_books = sorted(py_books, key=lambda x: x.title.lower())
    py_books = sorted(py_books, key=attrgetter('year'))
    py_books = sorted(py_books, key=attrgetter('rating'), reverse=True)

    # Re-rank
    for book in enumerate(py_books, start=1):
        book[1].rank = book[0]

    return py_books


def main():
    books = load_data()
    display_books(books, limit=5, year=2017)
    """If done correctly, the previous function call should display the
    output below.
    """


if __name__ == "__main__":
    main()

"""
[001] Python Tricks (2017)
      Bader, Dan 4.74
[002] Mastering Deep Learning Fundamentals with Python (2019)
      Wilson, Richard 4.7
[006] Python Programming (2019)
      Fedden, Antony Mc 4.68
[007] Python Programming (2019)
      Mining, Joseph 4.68
[009] A Smarter Way to Learn Python (2017)
      Myers, Mark 4.66
"""
