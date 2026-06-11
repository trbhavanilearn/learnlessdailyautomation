import pytest
import allure
from config import BASE_URL, PASSWORD

@allure.epic("LearnLessDaily Website")
@allure.feature("Content Validation - Mobile Number")
@allure.story("Verify Contact Number ")
@allure.title("Validate Contact Number")
@pytest.mark.sanity
def test_contact_number(page):
    page.goto(BASE_URL)
    content = page.content()
    assert "7418887599" in content