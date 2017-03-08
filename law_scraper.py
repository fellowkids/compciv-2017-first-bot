from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

HOMEPAGE_URL = 'https://law.stanford.edu/events/'



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


    d = {'url': evsoup.find('a', text='Find out more').attrs['href']}
    for k, sel in extracts:
        d[k] = ' '.join(e.get_text().strip() for e in evsoup.select(sel))

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

