import pytest
import allure
from config import BASE_URL, PASSWORD

@allure.epic("LearnLessDaily Website")
@allure.feature("HTTP homepage Validation Response")
@allure.story("Verify Homepage HTML working")
@allure.title("Validate Homepage HTML working")
@allure.tag("SMOKE")
@pytest.mark.smoke
def test_homepage_response(page):

    response = page.goto(
        BASE_URL
    )

    assert response.status == 200

    print(response.status)