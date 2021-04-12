from bs4 import BeautifulSoup
from HTML.locators.quotes_page_locators import QuotesPageLocators
from HTML.parsers.quote import QuoteParser


class QuotesPage:
    def __init__(self, page):
        self.html_dom = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        quote_tags = self.html_dom.select(QuotesPageLocators.QUOTE)
        return [QuoteParser(e) for e in quote_tags]
