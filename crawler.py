import sys
from bs4 import BeautifulSoup
import requests
import json
import datetime
from crawl_confi import BASE_LINK
from parser1 import Advertisement


class LinkCrawler:
    def __init__(self, link=BASE_LINK):
        self.link = link

    def get_page(self, url):
        response = requests.get(url)
        if response:
            return response
        else:
            raise ConnectionError('connection was failed')

    def get_links(self, html_doc):
        soup = BeautifulSoup(html_doc, 'html.parser')
        return soup.find_all('a', attrs={'class': 'product-card__link-overlay'})

    def start(self, url=BASE_LINK):
        page = self.get_page(url)
        links = self.get_links(page.text)
        for i in links:
            print(i.get('href'))

        self.store([i.get('href') for i in links])
        print('status code : ', page.status_code)
        print(f'total : {len(links)}')

    @classmethod
    def store(self, data):
        # now_time = datetime.datetime.now().strftime('%H%M')
        with open(f'links/file.json', 'w') as file:
            file.write(json.dumps(data))



class DataCrawler:

    def __init__(self):
        self.links = self.__load_links()
        self.parser = Advertisement()

    def __load_links(self):
        with open('links/file.json', 'r') as file:
            links = json.loads(file.read())
            return links

    def start(self):
        for link in self.links:
            response = requests.get(link)
            data = self.parser.parse(response.text)
            print(data)


