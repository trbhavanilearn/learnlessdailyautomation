import pytest
import allure
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from config import BASE_URL, PASSWORD

@allure.epic("LearnLessDaily Website")
@allure.feature("Webpage open")
@allure.story("Verify the website is up and running")
@pytest.mark.smoke
@pytest.mark.regression
@allure.title("Validate Login")
def test_valid_users():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False  # True = hidden browser, False = visible browser
        )
        page = browser.new_page()
        login = LoginPage(page)
        print("LoginPage object created")
        page.goto(BASE_URL)
        # Login actions here
        browser.close()