from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

HOMEPAGE_URL = 'https://law.stanford.edu/events/'
FOOD_PATTERNS = ['food', 'refreshments',
                 'lunch', 'dinner', 'dessert',
                 'cookies', 'meal', 'breakfast']


def extract_event(evsoup):
    """
    soup is a BeautifulSoup thing

    Returns a dictionary, with :title, :description,
            :url, :address, :datetime, :venue
    """
    extracts = (('title', '.tribe-events-list-event-title'),
               ('datetime', '.published.time-details'),
               ('venue', '.tribe-events-venue-details .org a'),
               ('address', '.tribe-street-address'),
               ('city', '.tribe-locality'),
               ('state', '.tribe-region'),
               ('description', '.entry-summary'),)


    # for k, sel in extracts:
    #     d[k] = ' '.join(e.get_text().strip() for e in evsoup.select(sel))

    d = {k: ''.join(e.get_text().strip() for e in evsoup.select(sel))}
    d['url'] = evsoup.find('a', text='Find out more').attrs['href']
    return d



def fetch_day_events(datestr):
    """
    datestr is YYYY-MM-DD

    Returns BeautifulSoup elements
    """
    url = urljoin(HOMEPAGE_URL, datestr)
    resp = requests.get(url, headers={'User-Agent': 'i like food'})
    soup = BeautifulSoup(resp.text, 'lxml')

    return [extract_event(el) for el
                              in soup.select('.tribe-events-day-time-slot')
                              if el.get_text().strip()]


def has_food(text):
    """
    text is a str

    returns True or False
    """
    return any(food in text.lower() for food in FOOD_PATTERNS)

