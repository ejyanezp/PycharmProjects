import logging
from selenium import webdriver

from pages.login_page import LoginPage
from pages.left_pane import LeftPane

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG,
                    filename='fore_flight_scrapper.log')
logger = logging.getLogger('flight_scraping')

logger.info('Entering into the flights App')
browser = webdriver.Chrome(executable_path=' ')
login_page = LoginPage(browser)
login_page.login()

left_pane = LeftPane(browser)
left_pane.go_flights()
