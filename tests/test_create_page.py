from pages.login_page import LoginPage


def test_adding_pet(browser):
    page = LoginPage(browser)
    page.open()
    (page.go_to_login("Jeron1mo@gmail.com").
     go_to_password("Ant10Ant10").
     go_to_btn().
     adding_pet_btn().
     fill_name("Ziggy").
     select_type().
     choose_type().
     create_gender().
     choose_gender().
     submit_create())

    browser.save_screenshot("result8.png")
