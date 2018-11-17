import os
import requests
from urllib.parse import urlparse, urljoin

from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool 

pool = ThreadPool(10) 

website = "http://localhost:8080/tgnet/"

if not website.startswith("http"):
    website = "http://"+website
if not website.endswith("/"):
    websiste = website + "/"

home_url = urlparse(website)

scanned_urls = []
not_scanned_urls = [website]

def eligible(url):
    url = urlparse(url)
    if url.netloc != home_url.netloc:
        return False

    if r in scanned_urls or r in not_scanned_urls:
        return False

    return True

def get_parse(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    new_links = []

    for link in [h.get('href') for h in soup.find_all('a')]:
        if link is None or link.startswith('#'):
            continue
        else:
            if link.startswith('http'):
                if urlparse(link).scheme != home_url.scheme:
                    continue
                
            next_link = urljoin(url, link)
            new_links.append(next_link)

    return new_links


while len(not_scanned_urls) > 0:

    length = 10 if len(not_scanned_urls)>10 else len(not_scanned_urls)

    results = pool.map(get_parse, not_scanned_urls[0:length])
    results = [item for sublist in results for item in sublist]

    scanned_urls.extend(not_scanned_urls[0:length])
    not_scanned_urls = not_scanned_urls[length:]

    for r in results:
        if eligible(r):
            not_scanned_urls.append(r)

    for s in scanned_urls:
        print(s)
    print(len(scanned_urls))