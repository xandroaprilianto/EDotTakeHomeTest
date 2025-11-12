# 🧪 EDot Automation Testing

Automation testing project for **Web** and **Mobile** platforms using **Pytest**, **Allure**, and **Appium**.

## ⚙️ Environment Setup

### Requirements
- Python ≥ 3.10
- Appium Server ≥ 2.x
- Node.js ≥ 16.x
- Java SDK ≥ 11
- Android SDK / Emulator
- Allure Commandline

### Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
appium
```

## 🧭 Running Tests

### Run All Tests
```bash
pytest -v
```

### Run by Platform
```bash
pytest web/tests -v
pytest mobile/tests --platform android -v
pytest mobile/tests --platform ios -v
```

### Run by File / Test Case
```bash
pytest web/tests/companies/addCompaniesTests/addCompany_test.py -v
pytest mobile/tests/test_login.py --platform android -v
pytest mobile/tests/test_login.py::test_valid_login --platform android -v
```

## 📊 Allure Report
```bash
pytest -v --alluredir=reports
allure serve reports/
```

## 📱 Example Android Capabilities
```json
{
  "platformName": "Android",
  "deviceName": "emulator-5554",
  "appPackage": "id.edot.ework",
  "appActivity": "id.edot.onboarding.ui.splash.SplashScreenActivity",
  "automationName": "UiAutomator2",
  "noReset": true,
  "autoGrantPermissions": true
}
```

---
**Author:** Xandro Aprilianto
