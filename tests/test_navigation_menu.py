import pytest
import allure
from config import BASE_URL, PASSWORD


@allure.epic("LearnLessDaily Website")
@allure.feature("Menu Navigation")
@allure.story("Verify the Navigation across Menu is up and running")
@allure.title("Validate the Navigation across Menu is up and running")
@pytest.mark.smoke
def test_navigation_menu(page,pytestconfig):
    base_url=pytestconfig.getini(base_url)
    page.goto(base_url)
    menu_links = page.locator("nav a")
    count = menu_links.count()
    assert count > 0
    print(f"Menu Count: {count}")