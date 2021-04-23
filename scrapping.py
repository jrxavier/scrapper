
from scrappers import Scrapper


page = Scrapper(
    'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops')

print(page.getTitle())
