from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        print(e)

    return title


title = getTitle(url)
if title == None:
    print("Não consegui achar o titulo")
else:
    print("Valor do título: ", title)
