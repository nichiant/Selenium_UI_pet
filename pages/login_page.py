from .base_page import BasePage
from .locators import LoginPageLocators
from .profile_page import ProfilePage


class LoginPage(BasePage):
    def go_to_login(self, login):
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys(login)
        return self

    def go_to_password(self, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_PASS).send_keys(password)
        return self

    def go_to_btn(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_BTN).submit()
        return ProfilePage