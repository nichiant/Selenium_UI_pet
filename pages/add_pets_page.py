import time
from pages.base_page import BasePage
from pages.locators import AddingPetsLocators


class AddPetsPage(BasePage):
    def fill_name(self, name):
        self.browser.find_element(*AddingPetsLocators.CREATE_NAME).send_keys(name)
        return AddPetsPage

    def select_type(self):
        self.browser.find_element(*AddingPetsLocators.CREATE_TYPE).click()
        return AddPetsPage

    def choose_type(self):
        self.browser.find_element(*AddingPetsLocators.CHOOSE_TYPE).click()
        return AddPetsPage

    def fill_age(self, age):
        time.sleep(1)
        self.browser.find_element(*AddingPetsLocators.CREATE_AGE).send_keys(age)
        return AddPetsPage

    def create_gender(self):
        self.browser.find_element(*AddingPetsLocators.CREATE_GENDER).click()
        return AddPetsPage

    def choose_gender(self):
        self.browser.find_element(*AddingPetsLocators.CHOOSE_GENDER).click()
        return AddPetsPage

    def submit_create(self):
        time.sleep(1)
        self.browser.find_element(*AddingPetsLocators.SUBMIT_CREATE).click()

    def cancel_create(self):
        time.sleep(1)
        self.browser.find_element(*AddingPetsLocators.CANCEL_CREATE).click()