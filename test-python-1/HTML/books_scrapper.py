from bs4 import BeautifulSoup
import re
import requests


class HTMLLocator:
    NAME = 'article.product_pod h3 a'
    LINK = 'article.product_pod h3 a'
    PRICE = 'article.product_pod p.price_color'
    RATING = 'article.product_pod p.star-rating'


class ParsedItem:
    def __init__(self, page):
        self.html_parser = BeautifulSoup(page, 'html.parser')

    @property
    def title(self):
        link = self.html_parser.select_one(HTMLLocator.NAME)
        title = link.attrs['title']
        return title

    @property
    def price(self):
        price = self.html_parser.select_one(HTMLLocator.PRICE).string
        pattern = '([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, price)
        return float(matcher.group(1))

    @property
    def rating(self):
        rating_tag = self.html_parser.select_one(HTMLLocator.RATING)
        classes = rating_tag.attrs['class']
        rating = [r for r in classes if r != 'star-rating'][0]
        return rating


# Using the file 'books.html'
# html_file = open(file='books.html', mode='r', encoding="utf-8")
# page = str(html_file.readlines())
# html_file.close()
# parser = ParsedItem(page)
# print(parser.title)
# print(parser.rating)
# print(parser.price)
# print(page)

# Using an URL
page = requests.get('http://books.toscrape.com').content
parser = ParsedItem(page)
print(parser.title)
print(parser.rating)
print(parser.price)
