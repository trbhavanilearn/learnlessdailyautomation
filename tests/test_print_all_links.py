import pytest
import allure
import requests
from pages.login_page import LoginPage
from config import BASE_URL, PASSWORD

@allure.epic("LearnLessDaily Website")
@allure.feature("Link Validation")
@allure.story("Verify all hyperlinks are working")
@allure.title("Validate all links working")
@pytest.mark.smoke
@pytest.mark.regression
def test_print_all_links(page,base_url):

    #base_url = pytestconfig.getini(base_url)

    allure.dynamic.title("Validate All Links on LearnLessDaily Homepage")

    page.goto(base_url)
    links = page.locator("a")
    count = links.count()
    print(f"\nTotal Links Found: {count}")
    results = []
    broken_links = []
    for i in range(count):
        text = links.nth(i).inner_text().strip()
        href = links.nth(i).get_attribute("href")
        if not href:
            result = (
                f"Link {i+1} | "
                f"Text='{text}' | "
                f"No href attribute found"
            )
            print(result)
            results.append(result)
            continue
        if href.startswith("/"):
            href = BASE_URL.rstrip("/") + href
        try:
            response = requests.get(
                href,
                timeout=10,
                allow_redirects=True
            )
            status_code = response.status_code
            if status_code < 400:
                status = "WORKING ✅"
            else:
                status = "BROKEN ❌"
                broken_links.append(href)
            result = (
                f"Link {i+1} | "
                f"Text='{text}' | "
                f"URL='{href}' | "
                f"Status={status_code} | "
                f"{status}"
            )
            print(result)
            results.append(result)
        except Exception as e:
            broken_links.append(href)
            result = (
                f"Link {i+1} | "
                f"Text='{text}' | "
                f"URL='{href}' | "
                f"ERROR={str(e)}"
            )
            print(result)
            results.append(result)
    # Attach results to Allure Report
    allure.attach(
        "\n".join(results),
        name="Link Validation Report",
        attachment_type=allure.attachment_type.TEXT
    )

    # Capture Screenshot
    page.screenshot(
        path="screenshots/link_validation.png",
        full_page=True
    )

    allure.attach.file(
        "screenshots/link_validation.png",
        name="Homepage Screenshot",
        attachment_type=allure.attachment_type.PNG
    )

    # Final Validation
    assert len(broken_links) == 0, (
        f"Broken Links Found: {broken_links}"
    )