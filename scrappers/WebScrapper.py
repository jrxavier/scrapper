from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup, SoupStrainer
from scrappers import Scrapper
import requests


class WebScrapper(object):

    def __init__(self):
        self.url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
        self.content = None

        try:
            response = requests.get(self.url)
            if self.content == None:
                self.content = response.content
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)

    def getSoupStrainer(self, caracter):
        tagsA = SoupStrainer(caracter)
        soup = BeautifulSoup(self.content, 'lxml', parse_only=tagsA)
        return soup

    def getSoup(self):
        soup = BeautifulSoup(self.content, 'lxml')
        return soup
