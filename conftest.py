import sys
import os
import pytest
import shutil

sys.path.insert(0, os.path.abspath("."))

@pytest.fixture(scope="function")
def context(browser):
    # Create browser context and enable video recording
    context = browser.new_context(
        record_video_dir="videos/"
    )

    # Start Playwright tracing
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )
    yield context
    # Stop tracing and save trace file
    context.tracing.stop(
        path="traces/trace.zip"
    )

    # Close browser context
    context.close()

# conftest.py


def pytest_sessionstart(session):

    allure_results = "reports/allure-results"

    os.makedirs(allure_results, exist_ok=True)

    files_to_copy = [
        "environment.properties",
        "categories.json",
        "executor.json"
    ]

    for file in files_to_copy:

        source = f"allure-config/{file}"
        destination = f"{allure_results}/{file}"

        if os.path.exists(source):
            shutil.copy(source, destination)