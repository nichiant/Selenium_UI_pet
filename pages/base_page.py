from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.url = "http://34.141.58.52:8080/#/login"
        self.browser.implicitly_wait(10)

    def open(self):
        self.browser.get(self.url)

