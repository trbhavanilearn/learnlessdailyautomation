import pytest
import allure
from config import BASE_URL, PASSWORD

@allure.epic("LearnLessDaily Website")
@allure.feature("Mobile View Response")
@allure.story("Verify Mobile View ")
@allure.title("Validate Mobile View")
@pytest.mark.regression
def test_mobile_view(page,base_url):
    #base_url=pytestconfig.getini(base_url)
    page.set_viewport_size(
        {
            "width": 375,
            "height": 667
        }
    )

    page.goto(base_url)
    page.screenshot(
        path="screenshots/mobile.png",
        full_page=True
    )
    assert page.locator("body").is_visible()