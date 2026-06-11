import pytest
import allure
from config import BASE_URL, PASSWORD

@allure.epic("LearnLessDaily Website")
@allure.feature("Buttons")
@allure.story("Verify the Buttons running")
@allure.title("Button Validations")
@pytest.mark.regression
def test_validate_buttons(page,pytestconfig):
    base_url=pytestconfig.getini(base_url)
    page.goto(BASE_URL)
    buttons = page.locator("button")
    count = buttons.count()
    print(f"Total Buttons: {count}")
    for i in range(count):
        button = buttons.nth(i)
        print(button.text_content())
        assert button.is_visible()
        assert button.is_enabled()