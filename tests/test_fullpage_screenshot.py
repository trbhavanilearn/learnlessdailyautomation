import pytest
import allure
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from config import BASE_URL, PASSWORD

@allure.epic("LearnLessDaily Website")
@allure.feature("Checking fullpage loading")
@allure.story("Verify the website is complete")
@allure.title("Validate the page is visible")
@pytest.mark.smoke
@pytest.mark.regression
def test_full_page_screenshot(page):

    page.goto(BASE_URL)

    page.screenshot(
        path="screenshots/homepage_full.png",
        full_page=True
    )