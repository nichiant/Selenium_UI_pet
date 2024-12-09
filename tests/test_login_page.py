from pages.login_page import LoginPage

def test_go_to_login(browser):
    page = LoginPage(browser)
    page.open()
    page.go_to_login("Jeron1mo@gmail.com")
    page.go_to_password("Ant10Ant10")
    page.go_to_btn()


    browser.save_screenshot('result6.png')
