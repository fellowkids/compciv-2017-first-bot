from datetime import datetime
from os.path import exists, getmtime, join
from os import makedirs
import requests
from requests.exceptions import Timeout, TooManyRedirects, RequestException
from sys import stderr
from slugify import slugify_filename
from urllib.parse import urlparse



def get_page(url):
    destname = url_to_filename(url)
    if valid_cache(destname):
        with open(destname, 'r') as f:
            return f.read()
    else:
        try:
            resp = requests.get(url, headers={'User-Agent': 'i like food'})
        except (Timeout, TooManyRedirects, RequestException) as e:
            stderr.write("{url} had {err}\n".format(err=e, url=url))
        else:
            if resp.status_code == 200:
                with open(destname, 'w') as f:
                    f.write(resp.text)
            return resp.text



def url_to_filename(url):
    """
    url is a string, e.g. 'https://law.stanford.edu/events/hello-world'

    Returns string representing path:
    law.stanford.edu/events_hello-world
    """
    purl =  urlparse(url)
    fpath = slugify_filename(purl.path + purl.params + purl.query + purl.fragment)
    return join(purl.netloc, fpath )


def valid_cache(filename):
    """
    returns True if filename exists and is less than 1 day old
    """
    return exists(filename) and (datetime.now().timestamp() - getmtime(filename) < 60*60*24):



