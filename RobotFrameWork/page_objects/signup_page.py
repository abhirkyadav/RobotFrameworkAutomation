class YahooSignUPPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = "//input[@id='usernamereg-firstName']"
        self.last_name_input = "//input[@id='usernamereg-lastName']"
        self.email_input = "//input[@id='usernamereg-email']"
        self.birth_year_input = "//input[@id='usernamereg-birthYear']"
        self.next_button = "//button[@name='signup']"

    def enter_first_name(self, first_name):
        self.driver.find_element("xpath", self.first_name_input).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element("xpath", self.last_name_input).send_keys(last_name)

    def enter_email(self, email):
        self.driver.find_element("xpath", self.email_input).send_keys(email)

    def enter_birth_year(self, birth_year):
        self.driver.find_element("xpath", self.birth_year_input).send_keys(birth_year)

    def click_next_button(self):
        self.driver.find_element("xpath", self.next_button).click()

