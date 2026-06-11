import pytest
import allure
from config import BASE_URL, PASSWORD

@allure.epic("LearnLessDaily Website")
@allure.feature("Images Validation")
@allure.story("Verify all Social links are working")
@allure.title("Validate all social links working")
@pytest.mark.regression
def test_images_loaded(page,base_url):
    #base_url=pytestconfig(base_url)
    page.goto(base_url)
    images = page.locator("img")
    count = images.count()
    print(f"Images Found: {count}")
    assert count > 0
    for i in range(count):
        image = images.nth(i)
        assert image.is_visible()