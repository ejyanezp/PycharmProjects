from HTML.locators.book_locators import *
from bs4 import BeautifulSoup


class BookParser:

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent: BeautifulSoup):
        self.parent = parent

    def __repr__(self):
        return f'<Book title: {self.title}, rating: {self.rating}, price: {self.price}>'

    @property
    def title(self):
        return self.parent.select_one(BookAttribLocators.TITLE).attrs['title']

    @property
    def link(self):
        return self.parent.select_one(BookAttribLocators.LINK).attrs['href']

    @property
    def rating(self):
        str_rating = self.parent.select_one(BookAttribLocators.RATING).attrs['class'][1]
        # use dictionary .get method to avoid exception.
        return BookParser.RATINGS.get(str_rating, 0)  # returns 0 (default) if key does not exist

    @property
    def price(self):
        return self.parent.select_one(BookAttribLocators.PRICE).string

