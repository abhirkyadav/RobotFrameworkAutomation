from yahoo_keywords import YahooKeywords

class YahooLibrary:
    def __init__(self):
        self.keywords = YahooKeywords()

    def open_browser_and_go_to_url(self, browser, url):
        self.keywords.open_browser_and_go_to_url(browser,url)

    def click_sign_in_button(self):
        self.keywords.click_sign_in_button()

    def click_create_a_account_button(self):
        self.keywords.click_create_a_account_button()

    def perform_sign_up(self, firstName, lastName, email, birthYear):
        self.keywords.perform_sign_up(firstName, lastName, email, birthYear)

    def close_browser(self):
        self.keywords.close_browser()
