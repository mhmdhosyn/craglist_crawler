import json
from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup

from config import BASE_LINK


class CrawlBase(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def store(self, data):
        pass


class LinkCrawler(CrawlBase):

    def __init__(self, cities, link=BASE_LINK):
        self.cities = cities
        self.link = link

    def get_page(self, url, start=0):
        try:
            response = requests.get(url + str(start))
        except:
            return None
        return response

    def find_links(self, html_doc):
        soup = BeautifulSoup(html_doc, 'html.parser')
        # content = soup.find('div', attrs={'class': 'content'})
        # adv_list = soup.find_all('li', attrs={'class': 'result-row'})
        return soup.find_all('a', attrs={'class': 'hdrlnk'})

    def start_crawl_city(self, url):
        start = 0
        crawl = True
        adv_links = list()
        while crawl:
            response = self.get_page(url, start)
            if response is None:
                crawl = False
                continue
            new_links = self.find_links(response.text)
            adv_links.extend(new_links)
            start += 120
            crawl = bool(len(new_links))

        return adv_links

    def start(self):
        adv_links = list()
        for city in self.cities:
            links = self.start_crawl_city(self.link.format(city))
            print(f'{city} total: {len(links)}')
            adv_links.extend(links)
        self.store([li.get('href') for li in adv_links])

    def store(self, data):
        with open("data/data.json", "w") as f:
            f.write(json.dumps(data))


class DataCrawler(CrawlBase):
    pass
