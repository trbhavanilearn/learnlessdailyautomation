import pytest
import allure
from config import BASE_URL, PASSWORD


@allure.epic("LearnLessDaily Website")
@allure.feature("Footer")
@allure.story("Verify the footer links working")
@allure.title("Footer Validation")
@pytest.mark.sanity
def test_footer_visible(page):
    page.goto(BASE_URL)
    footer = page.locator("footer")
    assert footer.is_visible()