from pages.base_page import BasePage
from .add_pets_page import AddPetsPage
from .edit_pet_page import EditInfoPetPage
from .locators import ProfilePageLocators


class ProfilePage(BasePage):

    def adding_pet_btn(self):
        self.browser.find_element(*ProfilePageLocators.ADDING_PET).click()
        return AddPetsPage

    def edit_info_pet_btn(self):
        self.browser.find_element(*ProfilePageLocators.EDIT_PET).click()
        return EditInfoPetPage

    def delete_info_pets(self):
        self.browser.find_element(*ProfilePageLocators.DELETE_PET).click()

    def check_name(self, name1):
        assert self.browser.find_element(*ProfilePageLocators.NAME).get_text() == name1

