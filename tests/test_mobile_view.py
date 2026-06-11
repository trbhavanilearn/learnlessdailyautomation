import pytest
import allure
from config import BASE_URL, PASSWORD

@allure.epic("LearnLessDaily Website")
@allure.feature("Mobile View Response")
@allure.story("Verify Mobile View ")
@allure.title("Validate Mobile View")
@pytest.mark.regression
def test_mobile_view(page):

    page.set_viewport_size(
        {
            "width": 375,
            "height": 667
        }
    )

    page.goto(BASE_URL)
    page.screenshot(
        path="screenshots/mobile.png",
        full_page=True
    )
    assert page.locator("body").is_visible()