import pytest
import allure
from config import BASE_URL, PASSWORD

@allure.epic("LearnLessDaily Website")
@allure.feature("Social Links Validation")
@allure.story("Verify all Social links are working")
@allure.title("Validate all social links working")
@pytest.mark.regression
def test_social_media_links(page,pytestconfig):
    base_url=pytestconfig.getini(base_url)
    page.goto(base_url)
    links = page.locator("a")
    count = links.count()
    social_sites = [
        "linkedin",
        "youtube",
        "facebook",
        "instagram",
        "whatsapp"
    ]
    for i in range(count):
        href = links.nth(i).get_attribute("href")
        if href:
            for site in social_sites:
                if site in href.lower():
                    print(f"Found {site}: {href}")