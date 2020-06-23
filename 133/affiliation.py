import re

url = 'https://www.amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/?keywords=war+of+art'
url4 = 'https://www.amazon.co.uk/Pragmatic-Programmer-Andrew-Hunt/dp/020161622X'
url5 = 'https://www.amazon.com.au/Python-Cookbook-3e-David-Beazley/dp/1449340377/'
url6 = 'https://www.amazon.com/fake-book-with-longer-asin/dp/1449340377000/'

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