from HTML.locators.quote_locators import QuoteLocators
from bs4 import BeautifulSoup


class QuoteParser:
    def __init__(self, parent: BeautifulSoup):
        self.parent = parent

    def __repr__(self):
        return f'<Quote {self.content}, by {self.author}>'

    @property
    def content(self):
        return self.parent.select_one(QuoteLocators.CONTENT).string

    @property
    def author(self):
        return self.parent.select_one(QuoteLocators.AUTHOR).string

    @property
    def tags(self):
        return [e.string for e in self.parent.select(QuoteLocators.TAGS)]

