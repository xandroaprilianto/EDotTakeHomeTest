from selenium.webdriver.common.by import By
from ..base_page import BasePage

class LoginPage(BasePage):
    UseEmailORUsername_BTN = (By.XPATH, "//button[contains(.,'Use Email or Username')]")
    Username_TXTFIELD = (By.NAME, "username")
    Password_TXTFIELD = (By.NAME, "password")
    Login_BTN = (By.XPATH, "//button[contains(.,'Log In')]")
    Greetings_TXTTitle = (By.XPATH, "//span[contains(.,'Welcome Back') or contains(.,'Selamat Datang Kembali')]")

    def click_useEmailorUsernameBTN(self):
        self.find(self.UseEmailORUsername_BTN).click()

    def input_username(self, text):
        self.type(self.Username_TXTFIELD, text)

    def click_loginBTN(self):
        self.find(self.Login_BTN).click()

    def input_password(self, text):
        self.type(self.Password_TXTFIELD, text)

    def verify_LoginSuccess(self):
        return self.find(self.Greetings_TXTTitle).is_displayed()