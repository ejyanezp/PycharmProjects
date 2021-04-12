import logging
from selenium import webdriver

from locators.fore_flight_locators import ForeFlightLocators

# Get a child logger
logger = logging.getLogger('flight_scraping.left_pane')


class LeftPane:
    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser

    def go_flights(self):
        web_element = self.browser.find_element_by_css_selector(ForeFlightLocators.MENU_FLIGHTS)
        web_element.click()
