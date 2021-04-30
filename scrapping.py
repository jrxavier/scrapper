
from scrappers import WebScrapper
import re

ws = WebScrapper()

# Buscando na pagina apenas as tags de img
bs = ws.getSoupStrainer("img")
# print(bs.prettify())

# print(bs.img.has_attr('alt'))

bs = ws.getSoup()

# Procurando imagens que tenham a classe identificada abaixo:
imagens = bs.find_all("img", class_="img-responsive")
for imagen in imagens:
    print(imagen)

# Procurando um p que tenha a classe "pull-right" e o texto de "9 reviews"
imagens = bs.find_all("p", class_="pull-right", text="9 reviews")
for imagen in imagens:
    print(imagen)

print("#####################")
# Pesquisa por atributos, limitado a 1 item
elementos = bs.find_all(
    "img", attrs={'alt': "item"}, limit=1)
for el in elementos:
    print(el)

print("#####################")
# Pesquisa usando regular expression
elementos = bs.find_all(
    "p", class_="pull-right", text=re.compile(r'reviews'))
for el in elementos:
    print(el)

print("#####################")
# Pesquisa apenas usando regular expression
elementos = bs.find_all(text=re.compile(r'reviews'))
for el in elementos:
    print(el)

# Trabalhando com dados dos cartões
print("#####################")
cards = bs.find_all("div", class_="col-sm-4")
for card in cards:
    print(card)
