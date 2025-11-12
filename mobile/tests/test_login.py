import time

from mobile.conftest import appium_driver
# import allure
#
# @allure.feature("Login")
# @allure.story("Valid login flow")
def test_valid_login(appium_driver):
    driver = appium_driver
    # allure.attach("App launched", name="Launch", attachment_type=allure.attachment_type.TEXT)

    # Contoh interaksi
    companyID_TXTField = driver.find_element("id", "id.edot.ework:id/tv_company_id")
    username_TXTField = driver.find_element("id", "id.edot.ework:id/tv_username")
    password_TXTField = driver.find_element("id", "id.edot.ework:id/tv_password")
    login_BTN = driver.find_element("id", "id.edot.ework:id/button_text")

    companyID_TXTField.send_keys("5049209")
    username_TXTField.send_keys("qatestsalesman")
    password_TXTField.send_keys("it.QA2025")
    login_BTN.click()
    time.sleep(30)

    # Assertion
    # success_message = driver.find_element("accessibility id", "welcomeMessage")
    # assert success_message.is_displayed()
