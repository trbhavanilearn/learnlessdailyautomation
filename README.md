# 🚀 LearnLessDaily Automation Framework

## 📌 Project Overview

This project is built using:

* 🐍 Python
* 🎭 Playwright
* 🧪 Pytest
* 📊 Allure Reports
* 🏗️ Page Object Model (POM)

The framework automates validation of the LearnLessDaily website including:

* Homepage Validation
* Navigation Validation
* Link Validation
* Screenshot Capture
* UI Verification
* Allure Reporting
* Future CI/CD Integration

---

# 📂 Project Structure

```text
learnlessdailyautomation/
│
├── pages/
│   ├── __init__.py
│   └── login_page.py
│
├── tests/
│   ├── __init__.py
│   └── test_login.py
│
├── screenshots/
│
├── reports/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── config.py
└── README.md
```

---

# ⚙️ Environment Setup

## Create Virtual Environment

```bash
python -m venv pwvenv
```

Activate:

### Windows

```bash
pwvenv\Scripts\activate
```

### Git Bash

```bash
source pwvenv/Scripts/activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install pytest
pip install playwright
pip install pytest-playwright
pip install allure-pytest
pip install requests
```

Install Browser:

```bash
playwright install
```

---

# 📋 requirements.txt

```text
pytest
playwright
pytest-playwright
allure-pytest
requests
```

---

# 🔧 Verify Installation

```bash
pytest --version
```

```bash
playwright --version
```

---

# 🏗️ Page Object Model Example

## pages/login_page.py

```python
class LoginPage:

    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()
```

---

# 🧪 Sample Test

## tests/test_login.py

```python
import pytest
import allure

from pages.login_page import LoginPage


@allure.title("Verify Homepage")
@pytest.mark.smoke
def test_homepage(page):

    login = LoginPage(page)

    login.navigate("https://learnlessdaily.com")

    assert "Learn" in login.get_title()
```

---

# 🎯 Pytest Markers

## pytest.ini

```ini
[pytest]

markers =
    smoke: Smoke Test Cases
    sanity: Sanity Test Cases
    regression: Regression Test Cases
```

---

# ▶️ Execution Commands

## Run All Tests

```bash
pytest
```

---

## Verbose Mode

```bash
pytest -v
```

---

## Run Single Test

```bash
pytest tests/test_login.py
```

---

## Run Specific Method

```bash
pytest tests/test_login.py::test_homepage
```

---

## Run Smoke Tests

```bash
pytest -m smoke
```

---

## Run Sanity Tests

```bash
pytest -m sanity
```

---

## Run Regression Tests

```bash
pytest -m regression
```

---

# 📸 Screenshot Capture

```python
page.screenshot(
    path="screenshots/homepage.png",
    full_page=True
)
```

---

# 🌐 Full Page Screenshot

```python
page.screenshot(
    path="screenshots/fullpage.png",
    full_page=True
)
```

---

# 🔍 Print All Links

```python
links = page.locator("a")

count = links.count()

for i in range(count):

    text = links.nth(i).inner_text()

    href = links.nth(i).get_attribute("href")

    print(text, href)
```

---

# 🔗 Validate Broken Links

```python
import requests

response = requests.get(url)

assert response.status_code < 400
```

---

# 🎭 Useful Playwright Commands

## Open URL

```python
page.goto(url)
```

---

## Click

```python
page.click("text=Login")
```

---

## Fill Text

```python
page.fill("#username", "admin")
```

---

## Press Key

```python
page.press("#search", "Enter")
```

---

## Wait

```python
page.wait_for_timeout(3000)
```

---

## Current URL

```python
print(page.url)
```

---

## Page Title

```python
print(page.title())
```

---

## Take Screenshot

```python
page.screenshot(path="sample.png")
```

---

# 📊 Allure Reporting

## Execute Tests

```bash
pytest --alluredir=reports/allure-results
```

---

## Generate Report

```bash
allure generate reports/allure-results --clean
```

---

## Open Report

```bash
allure serve reports/allure-results
```

---

# 📎 Allure Attachments

## Attach Screenshot

```python
allure.attach.file(
    "screenshots/homepage.png",
    name="Homepage",
    attachment_type=allure.attachment_type.PNG
)
```

---

## Attach Text

```python
allure.attach(
    "Execution Successful",
    name="Execution Log",
    attachment_type=allure.attachment_type.TEXT
)
```

---

# 🏆 Common Assertions

## Verify Title

```python
assert page.title() == "Expected Title"
```

---

## Verify URL

```python
assert page.url == expected_url
```

---

## Verify Text

```python
assert "Courses" in page.content()
```

---

## Verify Element Visible

```python
assert page.locator("button").is_visible()
```

---

# 🐞 Troubleshooting

## Import Error

```text
ModuleNotFoundError
```

Solution:

```python
from pages.login_page import LoginPage
```

Ensure:

```text
pages/
├── __init__.py
├── login_page.py
```

---

## Browser Not Found

```text
Executable doesn't exist
```

Run:

```bash
playwright install
```

---

## Allure Command Not Found

Install:

```bash
npm install -g allure-commandline
```

Verify:

```bash
allure --version
```

---

# 🚀 Future Enhancements

* Jenkins Integration
* GitHub Actions
* Azure DevOps
* Email Reports
* Slack Notifications
* Parallel Execution
* Data Driven Testing
* API Automation
* Database Validation
* Scheduled Hourly Execution

---

# 📈 Automation Coverage

| Module                | Status |
| --------------------- | ------ |
| Homepage Validation   | ✅      |
| Link Validation       | ✅      |
| Navigation Validation | ✅      |
| Screenshot Capture    | ✅      |
| Allure Reporting      | ✅      |
| Smoke Suite           | ✅      |
| Regression Suite      | ✅      |
| POM Framework         | ✅      |

---

# 💡 Learning Goals

✔ Understand Playwright

✔ Understand Pytest

✔ Understand Allure

✔ Build POM Framework

✔ Generate Reports

✔ Validate Real Websites

✔ Prepare for Enterprise Automation Projects

---

## 🎉 Happy Automating!

Built with ❤️ using Python + Playwright + Pytest + Allure
