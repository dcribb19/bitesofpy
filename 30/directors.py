import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve
import numpy as np 

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = '/tmp'
# added
if not os.path.exists(TMP):
    os.mkdir(TMP)

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movies = defaultdict(list)
    with open(local, encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                year = int(row['title_year'])
            except ValueError:
                year = 0
            score = float(row['imdb_score'])
            if year >= 1960:
                movies[row['director_name']].append(Movie(row['movie_title'], year, score))
    return movies


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    scores = []
    for movie in movies:
        scores.append(movie.score)
    return round(np.mean(scores), 1)
        

def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    average_scores = []
    for director, movies in directors.items():
        if len(movies) >= MIN_MOVIES:
            average_scores.append((director, calc_mean_score(movies)))
    return sorted(average_scores, key=lambda x: x[1], reverse=True)
