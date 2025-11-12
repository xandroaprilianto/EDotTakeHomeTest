import os
import json
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="android", help="Platform: android or ios")

@pytest.fixture(scope="session")
def appium_driver(request):
    platform = request.config.getoption("--platform")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    caps_file = os.path.join(base_dir, "drivers", f"{platform.lower()}_capabilities.json")

    with open(caps_file) as f:
        desired_caps = json.load(f)

    if platform.lower() == "android":
        options = UiAutomator2Options()
    elif platform.lower() == "ios":
        options = XCUITestOptions()
    else:
        raise ValueError("Unsupported platform. Use --platform android or ios.")

    # tambahkan capabilities ke options
    options.load_capabilities(desired_caps)

    # konek ke Appium server
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(10)

    yield driver
    driver.quit()
