import requests
from bs4 import BeautifulSoup

cached_so_url = 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'


def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    questions = soup.find_all('a', class_='question-hyperlink')
    questions = [question.text for question in questions]

    votes = soup.find_all('span', class_='vote-count-post')
    votes = [int(vote.text) for vote in votes]

    views = soup.find_all('div', class_='views')
    views = [view.text.strip().split()[0] for view in views]

    zipped_up = zip(questions, votes, views)

    return sorted([(z[0], z[1]) for z in zipped_up if z[2].endswith('m')],
                  key=lambda x: x[1], reverse=True
                  )
