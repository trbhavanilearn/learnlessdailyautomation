import pytest
import allure
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from datetime import datetime
from config import BASE_URL, PASSWORD

@allure.epic("LearnLessDaily Website")
@allure.feature("Checking fullpage loading")
@allure.story("Verify the website is complete")
@allure.title("Validate Fullpage screenshot visible")
@pytest.mark.smoke
@pytest.mark.regression
def test_full_page_screenshot(page,base_url):
    timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
    #base_url=pytestconfig.getini(base_url)
    page.goto(base_url)
    page.screenshot(
        path=f"screenshots/homepage_full_{timestamp}.png",
        full_page=True
    )
    screenshot = page.screenshot(full_page=True)
    allure.attach(
    screenshot,
    name="Homepage Screenshot",
    attachment_type=allure.attachment_type.PNG
   )
   """ allure.attach.file(
        "screenshots/homepage_full.png",
        name="Homepage Full Screenshot",
        attachment_type=allure.attachment_type.PNG
    )"""