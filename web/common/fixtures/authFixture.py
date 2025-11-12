import pytest
from web.pages.authLocator.loginLocator import LoginPage

@pytest.fixture
def do_login(driver):
    def _login():
        login = LoginPage(driver)
        login.open("https://esuite.edot.id")
        login.click_useEmailorUsernameBTN()
        login.input_username("it.qa@edot.id")
        login.click_loginBTN()
        login.input_password("it.QA2025")
        login.click_loginBTN()
        login.verify_LoginSuccess()
    return _login
