import requests
import logging
import time

from HTML.pages.books_page import BooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG,
                    filename='books_scrapper.log')
logger = logging.getLogger('scraping')
logger.info('Loading books list')

page_number = 1
all_books = []
start = time.time()
while True:
    page_start = time.time()
    print(f'Getting books in page {page_number}')
    url = f'http://books.toscrape.com/catalogue/page-{page_number}.html'
    page_content = requests.get(url).content
    page = BooksPage(page_content)
    if page_number >= page.page_count:
        break
    page_number += 1
    all_books += page.books
    print(f'Page took: {time.time() - page_start}, Books count: {len(all_books)}')
print(f'All took {time.time() - start}')


# for page_number in range(1, 50):
#    print(f'Getting books in page {page_number}')
#    url = f'http://books.toscrape.com/catalogue/page-{page_number}.html'
#    page_content = requests.get(url).content
#    page = BooksPage(page_content)
#    all_books += page.books
#    print(f'Books count: {len(all_books)}')

for book in all_books:
    print(book)

# print the bests books
print('\nBEST BOOKS')
best_books = sorted(all_books, key=lambda b: b.rating, reverse=True)[0:5]
for b in best_books:
    print(b)

# print the cheapest books
print('\nCHEAPEST BOOKS')
cheap_books = sorted(all_books, key=lambda b: b.price)[0:5]
for b in cheap_books:
    print(b)

# for the best books print the 5 cheapest, use a tuple in the lambda function
print('\nBEST & CHEAPEST BOOKS')
best_cheapest_books = sorted(all_books, key=lambda b: (5-b.rating, b.price))[0:5]
for b in best_cheapest_books:
    print(b)
