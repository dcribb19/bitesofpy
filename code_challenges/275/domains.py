from collections import Counter

from bs4 import BeautifulSoup
import requests

COMMON_DOMAINS = ("https://bites-data.s3.us-east-2.amazonaws.com/"
                  "common-domains.html")
TARGET_DIV = {"class": "middle_info_noborder"}


def get_common_domains(url=COMMON_DOMAINS):
    """Scrape the url return the 100 most common domain names"""
    response = requests.get(COMMON_DOMAINS)
    soup = BeautifulSoup(response.text, 'html.parser')
    domains = soup.find('div', class_=TARGET_DIV['class'])
    domains = domains.find_all('tr')
    return [domain.find_all('td')[2].text for domain in domains]


def get_most_common_domains(emails, common_domains=None):
    """Given a list of emails return the most common domain names,
       ignoring the list (or set) of common_domains"""
    if common_domains is None:
        common_domains = get_common_domains()
    c = Counter()
    for email in emails:
        _, domain = email.split('@')
        if domain not in common_domains:
            c[domain] += 1
    return c.most_common()
