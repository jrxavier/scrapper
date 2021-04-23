
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

from bs4 import BeautifulSoup
from scrappers import Scrapper


class Scrapper(object):

    def __init__(self, url):
        self.url = url
        self.bs = None

        try:
            html = urlopen(url)
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)
        try:
            if self.bs == None:
                self.bs = BeautifulSoup(html.read(), 'html.parser')
        except AttributeError as e:
            print(e)

    def getTitle(self):
        try:
            title = self.bs.body.h1
        except AttributeError as e:
            print(e)

        return title

    def getItens(self):
        try:
            title = self.bs.body.h1
        except AttributeError as e:
            print(e)

        return title
