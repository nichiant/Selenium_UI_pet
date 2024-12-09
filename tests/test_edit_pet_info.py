from pages.login_page import LoginPage


def test_edit_info(browser):
    page = LoginPage(browser)
    page.open()
    (page.go_to_login("Jeron1mo@gmail.com").
     go_to_password("Ant10Ant10").
     go_to_btn().
     edit_info_pet_btn().
     edit_pet_name("Funny123").
     edit_pet_type().
     choose_pet_type().
     edit_pet_age().
     edit_pet_gender().
     choose_pet_gender().
     save_pet_changes())
