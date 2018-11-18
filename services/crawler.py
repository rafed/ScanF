import os
import requests
from urllib.parse import urlparse, urljoin

from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool 

from model.website import Website
from model.page import Page

class Crawler:
    def __init__(self):
        self.pool = ThreadPool(10) 
        self.running = False
        
    def setup(self, url):
        if not url.startswith("http"):
            url = "http://"+url
        # if not url.endswith("/"):
        #     url = url + "/"
        self.url = url
        self.home_url = urlparse(self.url)
        self.scanned_urls = []
        self.not_scanned_urls = [self.url]


    def crawl(self):
        self.running = True
        
        while len(self.not_scanned_urls) > 0 and self.running is True:

            length = 10 if len(self.not_scanned_urls)>10 else len(self.not_scanned_urls)

            results = self.pool.map(self._get_parse, self.not_scanned_urls[0:length])
            results = [item for sublist in results for item in sublist]

            self.scanned_urls.extend(self.not_scanned_urls[0:length])
            self.not_scanned_urls = self.not_scanned_urls[length:]

            for r in results:
                if self._eligible(r):
                    self.not_scanned_urls.append(r)

            print(self.not_scanned_urls)
            for s in self.scanned_urls:
                print(s)
            print(len(self.scanned_urls))

        self.running = False


    def _get_parse(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        new_links = []

        for link in [h.get('href') for h in soup.find_all('a')]:
            if link is None or link.startswith('#'):
                continue
            else:
                if link.startswith('http'):
                    if urlparse(link).hostname != self.home_url.hostname:
                        continue
                    
                next_link = urljoin(url, link)
                new_links.append(next_link)

        return new_links

   
    def _eligible(self, url):
        parsed_url = urlparse(url)
        if parsed_url.hostname != self.home_url.hostname:
            return False

        if url in self.scanned_urls or url in self.not_scanned_urls:
            return False

        return True