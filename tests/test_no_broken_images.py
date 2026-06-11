import pytest
import allure
from config import BASE_URL, PASSWORD

@allure.epic("LearnLessDaily Website")
@allure.feature("Broken Images")
@allure.story("Verify Broken Image ")
@allure.title("Validate Broken Image")
@pytest.mark.regression
def test_no_broken_images(page,pytestconfig):
    base_url=pytestconfig.getini(base_url)
    page.goto(base_url)
    images = page.locator("img")
    count = images.count()
    for i in range(count):
        src = images.nth(i).get_attribute("src")
        print(src)
        assert src is not None