import logging
from selenium import webdriver

from locators.fore_flight_locators import ForeFlightLocators

# Get a child logger
logger = logging.getLogger('flight_scraping.login')


class LoginPage:

    HOME_URL = 'https://foreflight.com/'
    APP_URL = 'https://plan.foreflight.com'
    USER = 'eyanezprado@yahoo.com'
    PASSWORD = 'Learjet7411'

    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser

    def login(self):
        logger.info('Get HOME page')
        self.browser.get(LoginPage.HOME_URL)
        web_element = self.browser.find_element_by_css_selector(ForeFlightLocators.LOGIN_BUTTON_LOCATOR)
        login_url = web_element.get_attribute('href') + '&_ga=2.24847609.276137689.1613665228-903287096.1613274076'

        self.browser.get(login_url)
        logger.info(f'Get login Form at {self.browser.current_url}')
        web_element = self.browser.find_element_by_css_selector(ForeFlightLocators.USER_INPUT_FIELD)
        web_element.send_keys(LoginPage.USER)
        web_element = self.browser.find_element_by_css_selector(ForeFlightLocators.PASSWORD_INPUT_FIELD)
        web_element.send_keys(LoginPage.PASSWORD)
        web_element = self.browser.find_elements_by_css_selector(ForeFlightLocators.DO_LOGIN_BUTTON)
        web_element[1].click()

