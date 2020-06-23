import re

def generate_affiliation_link(url):
    url = re.sub(r'\S+/dp/', 'http://www.amazon.com/dp/', url)
    end = re.split(r'\S+/dp/\d+\w?', url)
    ending = '/?tag=pyb0f-20'
    
    if end[1] == '':
        return url + ending
    elif end[1] == '/':
        return url + ending.replace('/', '')
    else:
        return url.replace(end[1], ending)