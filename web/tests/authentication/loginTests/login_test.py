from web.common.config.conftest import driver
from web.pages.authLocator.loginLocator import LoginPage

def test_success_login(driver):
    login = LoginPage(driver)
    login.open("https://esuite.edot.id")
    login.click_useEmailorUsernameBTN()
    login.input_username("it.qa@edot.id")
    login.click_loginBTN()
    login.input_password("it.QA2025")
    login.click_loginBTN()
    login.verify_LoginSuccess()
    # assert "Google" in driver.title
