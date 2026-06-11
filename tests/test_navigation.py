import pytest
import allure
from pages.login_page import LoginPage
from config import BASE_URL, PASSWORD


@allure.epic("LearnLessDaily Website")
@allure.feature("Webpage open")
@allure.story("Verify the naviation links up and running is up and running")
@pytest.mark.smoke
def test_navigation_menu(page,pytestconfig):
    base_url=pytestconfig.getini(base_url)
    page.goto(base_url)
    menu_links = page.locator("nav a")
    count = menu_links.count()
    assert count > 0
    print(f"Menu Count: {count}")