import time
from pages.base_page import BasePage
from .locators import EditPageLocators
from .profile_page import ProfilePage


class EditInfoPetPage(BasePage):
    def edit_pet_name(self, name):
        self.browser.find_element(*EditPageLocators.CHANGE_NAME).clear().send_keys(name)
        return EditInfoPetPage

    def edit_pet_type(self):
        self.browser.find_element(*EditPageLocators.EDIT_TYPE).click()
        return EditInfoPetPage

    def choose_pet_type(self):
        self.browser.find_element(*EditPageLocators.CHOOSE_TYPE).click()
        return EditInfoPetPage

    def edit_pet_age(self, age):
        self.browser.find_element(*EditPageLocators.CHANGE_AGE).clear().send_keys(age)
        return EditInfoPetPage

    def edit_pet_gender(self):
        self.browser.find_element(*EditPageLocators.EDIT_GENDER).click()
        return EditInfoPetPage

    def choose_pet_gender(self):
        self.browser.find_element(*EditPageLocators.CHANGE_AGE).click()
        return EditInfoPetPage

    def save_pet_changes(self):
        time.sleep(1)
        self.browser.find_element(*EditPageLocators.SAVE_EDIT).click()
        return ProfilePage
