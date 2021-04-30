from urllib.error import HTTPError
from urllib.error import URLError
from urllib.robotparser import RobotFileParser
import requests

from bs4 import BeautifulSoup
from scrappers import Scrapper


class Scrapper(object):

    def __init__(self, url):
        self.url = url
        self.bs = None

        try:
            response = requests.get(self.url)
            content = response.content
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)
        try:
            if self.bs == None:
                self.bs = BeautifulSoup(content, "lxml")
        except AttributeError as e:
            print(e)

    def getTitle(self):
        try:
            title = self.bs.body.h1
        except AttributeError as e:
            print(e)

        return title

    def getCards(self):
        try:
            cards = self.bs.find_all(
                'div', class_='col-sm-4 col-lg-4 col-md-4')
        except AttributeError as e:
            print(e)

        return cards

    # Funcao interessante que permite avaliar se uma url está aberta para robô
    def roboTxt(self):
        par = RobotFileParser()
        par.set_url('https://www.samsclub.com/robots.txt')
        par.read()
        # return par.can_fetch('*', 'https://www.zomato.com/pt/brasilia')
        return par.can_fetch('*', 'https://www.samsclub.com/account')
