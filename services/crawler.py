import os
import requests
from urllib.parse import urlparse, urljoin

from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool 

from model.website import Website
from model.page import Page
from model.form import Form
from model.field import Field
from model.constraint import Constraint

from services.form_parser import FormParser

class Crawler:
    def __init__(self):
        self.pool = ThreadPool(10) 
        self.running = False
        
    def _setup(self, url):
        if not url.startswith("http"):
            url = "http://"+url
        # if not url.endswith("/"):
        #     url = url + "/"

        self.url = url
        self.home_url = urlparse(self.url)
        self.scanned_urls = []
        self.not_scanned_urls = [self.url]
        self.running = True

        website = Website.query.filter(Website.baseurl == self.home_url.netloc).first()

        if not website:
            website = Website(self.home_url.netloc, None)
            website.save_to_db()

        self.website_id = website.id

    def crawl(self, url):
        self._setup(url)

        while len(self.not_scanned_urls) > 0 and self.running is True:

            length = 10 if len(self.not_scanned_urls)>10 else len(self.not_scanned_urls)

            results = self.pool.map(self._get_links_and_forms_and_store, self.not_scanned_urls[0:length])
            results = [item for sublist in results for item in sublist]

            self.scanned_urls.extend(self.not_scanned_urls[0:length])
            self.not_scanned_urls = self.not_scanned_urls[length:]

            for r in results:
                if self._eligible(r):
                    self.not_scanned_urls.append(r)

        self.running = False


    def _get_links_and_forms_and_store(self, url):
        if Page.query.filter(Page.url == url).first():
            return []

        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        try:
            page = Page(self.website_id, url)
            page.save_to_db()
            self._get_forms(soup, page.id, url)
        except Exception as e:
            print("Row already exists", e)
        
        return self._get_links(url, soup)

    def _get_forms(self, soup, id, baseurl):
        forms = soup.findAll('form')
        for form in forms:
            parsed_form = FormParser(baseurl, form)

            if not parsed_form.get_fields(): continue

            formdb = Form(id, parsed_form.get_method(), parsed_form.get_action())
            formdb.save_to_db()

            for field in parsed_form.get_fields():
                fielddb = Field(formdb.id,  field['attributes']['type'],
                                            field['attributes']['name'],
                                            field['attributes']['value'])
                fielddb.save_to_db()

                for key, value in field['constraints'].items():
                    if value is None: continue
                    c = Constraint(fielddb.id, key, value)
                    c.save_to_db()
                
            #############
            #############
            #############


    def _get_links(self, baseurl, soup):
        new_links = []

        for link in [h.get('href') for h in soup.find_all('a')]:
            if link is None or link.startswith('#'):
                continue
            else:
                if link.startswith('http'):
                    if urlparse(link).hostname != self.home_url.hostname:
                        continue
                    
                next_link = urljoin(baseurl, link)
                new_links.append(next_link)

        return new_links

    def _eligible(self, url):
        parsed_url = urlparse(url)
        if parsed_url.hostname != self.home_url.hostname:
            return False

        if url in self.scanned_urls or url in self.not_scanned_urls:
            return False

        return True