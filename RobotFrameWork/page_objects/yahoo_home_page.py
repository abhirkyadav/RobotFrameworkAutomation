class YahooHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.sign_button = "//a[contains(@data-redirect-params,'signin')]"
        self.create_account_button = "//a[contains(@data-ylk,'signup')]"

    def click_sign_in_button(self):
        self.driver.find_element("xpath", self.sign_button).click()

    def click_create_a_account_button(self):
        self.driver.find_element("xpath", self.create_account_button).click()
