import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from setup.driver import DriverSetup
from page_objects.yahoo_home_page import YahooHomePage
from page_objects.signup_page import YahooSignUPPage

class YahooKeywords:

    def __init__(self):
        self.driver = None

    def open_browser_and_go_to_url(self, browser,url):
        self.driver = DriverSetup.start_browser(browser)
        self.home_page = YahooHomePage(self.driver)
        self.signup_page = YahooSignUPPage(self.driver)
        self.driver.get(url)

    def click_sign_in_button(self):
        self.home_page.click_sign_in_button()

    def click_create_a_account_button(self):
        self.home_page.click_create_a_account_button()

    def perform_sign_up(self, firstName, lastName, email, birthYear):
        self.signup_page.enter_first_name(firstName)
        self.signup_page.enter_last_name(lastName)
        self.signup_page.enter_email(email)
        self.signup_page.enter_birth_year(birthYear)
        self.signup_page.click_next_button()

    def close_browser(self):
        DriverSetup.quit_browser()