import pytest
import allure
import time
from config import BASE_URL, PASSWORD

@allure.epic("LearnLessDaily Website")
@allure.feature("Performance Loadpage")
@allure.story("Verify Homepage Loadtime ")
@allure.title("Validate Homepage loading Time")
@pytest.mark.sanity
def test_page_load_time(page,pytestconfig):
    base_url=pytestconfig.getini(base_url)
    start = time.time()
    page.goto(base_url)
    end = time.time()
    load_time = end - start
    print(f"Load Time: {load_time}")
    assert load_time < 10