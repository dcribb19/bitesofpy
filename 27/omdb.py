import json
import re

def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movies = []
    for file in files:
        with open(file) as json_file:
            movie = json.load(json_file)
            movies.append(movie)
    return movies


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for movie in movies:
        if 'Comedy' in movie['Genre']:
            return movie['Title']


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    nominations = {}
    for movie in movies:
        noms = 0
        s1 = re.findall(r'\d+\snominations', movie['Awards'])
        s2 = re.findall(r'Nominated for \d+', movie['Awards'])
        if len(s1) == 1:
            noms += int(s1[0].split()[0])
        if len(s2) == 1:
            noms += int(s2[0].split()[-1])
        nominations[noms] = movie['Title']
    
    return nominations[max(nominations.keys())]


def get_movie_longest_runtime(movies: list) -> str:
    longest = 0
    for movie in movies:
        run_time = int(movie['Runtime'].split()[0])
        if run_time > longest:
            longest = run_time

    # RETURN MOVIE NAME
    for movie in movies:
        if movie['Runtime'] == str(longest) + ' min':
            return movie['Title']
