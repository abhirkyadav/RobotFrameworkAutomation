from selenium import webdriver

class DriverSetup:
    driver = None

    @classmethod
    def start_browser(cls, browser='chrome'):
        if browser.lower() == 'chrome':
            cls.driver = webdriver.Chrome()
        elif browser.lower() == 'firefox':
            cls.driver = webdriver.Firefox()
        else:
            raise Exception("Unsupported browser!")
        
        cls.driver.maximize_window()
        return cls.driver

    @classmethod
    def quit_browser(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None  # Optional: clean up after quitting
