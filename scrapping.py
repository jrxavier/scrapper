
from scrappers import Scrapper


page = Scrapper(
    'https://webscraper.io/test-sites/e-commerce/allinone/computers')


items = page.getCards()

for item in items:
    price = item.h4.text
    description = item.p.text
    print(price)
    print(description)
