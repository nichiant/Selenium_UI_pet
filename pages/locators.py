from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")


class ProfilePageLocators:
    ADDING_PET = (By.XPATH, "(//div[@class='col-6']/button)[1]")
    EDIT_PET = (By.XPATH, "(//div[@class='product-list-action']/button)[1]")
    DELETE_PET = (By.XPATH, "((//div[@class='product-list-action']/button)[2]")
    CANCEL_DELETE = (By.XPATH, "//button[contains(@aria-label, 'No')]")
    NAME = (By.XPATH, "//div[@class='product-name']")

    CLEAR_LIST = (By.XPATH, "(//div[@class='col-6']/button)[2]")  # НЕ НАЖИМАТЬ!!!(удаляет весь профиль)


class AddingPetsLocators:
    CREATE_NAME = (By.XPATH, "//input[@id='name']")
    CREATE_TYPE = (By.XPATH, "//span[@id='typeSelector']")
    CHOOSE_TYPE = (By.XPATH, "(//li[@class='p-dropdown-item'])[1]")
    CREATE_AGE = (By.XPATH, "//span[@id='age']")
    CREATE_GENDER = (By.XPATH, "//span[@id='genderSelector']")
    CHOOSE_GENDER = (By.XPATH, "(//li[@class='p-dropdown-item'])[1]")
    SUBMIT_CREATE = (By.XPATH, "(//div[@class='p-card-footer']/button)[1]")
    CANCEL_CREATE = (By.XPATH, "(//div[@class='p-card-footer']/button)[2]")


class EditPageLocators:
    CHANGE_NAME = (By.XPATH, "//input[@id='name']")
    EDIT_TYPE = (By.XPATH, "//span[@id='typeSelector']")
    CHOOSE_TYPE = (By.XPATH, "(//li[@class='p-dropdown-item'])[1]")
    CHANGE_AGE = (By.XPATH, "//span[@id='age']")
    EDIT_GENDER = (By.XPATH, "//span[@id='genderSelector']")
    CHOOSE_GENDER = (By.XPATH, "(//li[@class='p-dropdown-item'])[1]")
    SAVE_EDIT = (By.XPATH, "//div[@class='p-card-footer']/button")
