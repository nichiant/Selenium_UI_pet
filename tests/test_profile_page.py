from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
from pages.edit_pet_page import EditInfoPetPage


def test_edit_pet(browser):
    # link = "http://34.141.58.52:8080/#/login"
    page = LoginPage(browser)
    page.open()
    page.go_to_login("Jeron1mo@gmail.com")
    page.go_to_password("Ant10Ant10")
    page.go_to_btn()

    # link = "http://34.141.58.52:8080/#/profile"
    # page = ProfilePage(browser)
    # page.open()
    # page.edit_info_pets_btn()




    browser.save_screenshot("result7.png")