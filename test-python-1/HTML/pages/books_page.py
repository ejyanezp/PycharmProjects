from bs4 import BeautifulSoup
import re
from HTML.locators.book_locators import BooksLocator
from HTML.parsers.book import BookParser


class BooksPage:
    def __init__(self, page):
        self.html_dom = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        book_list = self.html_dom.select(BooksLocator.BOOK)
        return [BookParser(e) for e in book_list]

    @property
    def page_count(self):
        str_count = self.html_dom.select_one(BooksLocator.PAGES_COUNT).string.strip()
        pattern = 'Page \d+ of (\d+)'
        match = re.search(pattern, str_count)
        return int(match.group(1))
