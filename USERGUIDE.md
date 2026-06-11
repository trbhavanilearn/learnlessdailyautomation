# User Guide

## Playwright + Pytest + Allure Reporting + Traceability Framework

---

# Overview

This framework combines:

* **Playwright** for browser automation
* **Pytest** for test execution
* **Allure Reports** for advanced reporting
* **Playwright Tracing** for debugging and audit trails
* **Video Recording** for execution playback
* **Screenshot Capture** for failure analysis

The framework provides complete execution traceability, making it easier to analyze failures and maintain test quality.

---

# Prerequisites

Before starting, ensure the following are installed:

| Tool       | Version |
| ---------- | ------- |
| Python     | 3.10+   |
| Pip        | Latest  |
| Playwright | Latest  |
| Pytest     | Latest  |
| Allure     | Latest  |

Verify installation:

```bash
python --version
pip --version
```

---

# Installation

## Install Required Packages

```bash
pip install pytest
pip install playwright
pip install pytest-playwright
pip install allure-pytest
```

## Install Browser Binaries

```bash
playwright install
```

---

# Installing Allure

## Windows (Using Scoop)

Install Scoop if not already installed.

```bash
scoop install allure
```

Verify installation:

```bash
allure --version
```

Expected output:

```text
2.x.x
```

---

# Framework Configuration

## Enable Playwright Tracing

Update `conftest.py`:

```python
import pytest


@pytest.fixture(scope="function")
def context(browser):

    context = browser.new_context(
        record_video_dir="videos/"
    )

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield context

    context.tracing.stop(
        path="traces/trace.zip"
    )

    context.close()
```

### What Tracing Captures

* Screenshots
* DOM snapshots
* Network activity
* User interactions
* Browser timeline
* Source files

---

## Create Page Fixture

```python
@pytest.fixture(scope="function")
def page(context):

    page = context.new_page()

    yield page

    page.close()
```

This fixture creates a fresh browser page for every test.

---

# Running Tests

Execute all tests:

```bash
pytest -v
```

Generated artifacts:

```text
videos/
traces/
```

---

# Viewing Playwright Trace

After test execution:

```bash
playwright show-trace traces/trace.zip
```

The Trace Viewer provides:

* Click history
* Network requests
* DOM snapshots
* Screenshots
* Console logs
* Execution timeline

---

# Allure Reporting

## Generate Allure Results

```bash
pytest --alluredir=reports/allure-results
```

Generated structure:

```text
reports/
└── allure-results/
```

---

## Launch Allure Dashboard

```bash
allure serve reports/allure-results
```

The report opens automatically in the default browser.

---

# Screenshot Attachments

Attach screenshots to Allure reports.

```python
import allure

page.screenshot(
    path="screenshots/homepage.png",
    full_page=True
)

allure.attach.file(
    "screenshots/homepage.png",
    name="Homepage Screenshot",
    attachment_type=allure.attachment_type.PNG
)
```

---

# Log Attachments

Attach execution logs to Allure.

```python
allure.attach(
    "Homepage loaded successfully",
    name="Execution Logs",
    attachment_type=allure.attachment_type.TEXT
)
```

---

# Automatic Screenshot on Failure

Add the following hook in `conftest.py`.

```python
import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs["page"]

        page.screenshot(
            path=f"screenshots/{item.name}.png",
            full_page=True
        )
```

Benefits:

* Captures failure evidence automatically
* Helps root-cause analysis
* Improves debugging efficiency

---

# Attach Trace Files to Allure

```python
allure.attach.file(
    "traces/trace.zip",
    name="Playwright Trace",
    attachment_type=allure.attachment_type.ZIP
)
```

This allows direct access to trace files from the Allure dashboard.

---

# Video Recording

Enable video recording:

```python
context = browser.new_context(
    record_video_dir="videos/"
)
```

Generated files:

```text
videos/
├── test1.webm
├── test2.webm
```

---

# Attach Videos to Allure

```python
allure.attach.file(
    "videos/test1.webm",
    name="Execution Video",
    attachment_type=allure.attachment_type.WEBM
)
```

---

# Executing Marker-Based Tests

## Smoke Tests

```bash
pytest -m smoke \
--alluredir=reports/allure-results
```

## Sanity Tests

```bash
pytest -m sanity \
--alluredir=reports/allure-results
```

## Regression Tests

```bash
pytest -m regression \
--alluredir=reports/allure-results
```

---

# Parallel Execution

Run tests in parallel:

```bash
pytest -n auto \
--alluredir=reports/allure-results
```

Benefits:

* Faster execution
* Better resource utilization
* Reduced feedback cycle

---

# Headed Mode Execution

Run browser in visible mode:

```bash
pytest --headed
```

Useful for:

* Debugging
* Demonstrations
* Troubleshooting

---

# Browser Selection

## Chromium

```bash
pytest --browser chromium
```

## Firefox

```bash
pytest --browser firefox
```

## WebKit

```bash
pytest --browser webkit
```

---

# Enterprise Execution Command

Recommended execution command:

```bash
pytest \
-v \
-s \
-n auto \
--browser chromium \
--alluredir=reports/allure-results
```

Generate report:

```bash
allure serve reports/allure-results
```

Open trace:

```bash
playwright show-trace traces/trace.zip
```

---

# Output Structure

After execution:

```text
project-root/
│
├── screenshots/
│   └── homepage.png
│
├── videos/
│   └── execution.webm
│
├── traces/
│   └── trace.zip
│
└── reports/
    └── allure-results/
```

---

# Best Practices

### Recommended

* Use page objects for maintainability.
* Capture screenshots only on failures.
* Attach traces for critical test failures.
* Use markers to organize suites.
* Execute regression suites in parallel.
* Store reports as CI/CD artifacts.

### Avoid

* Hard-coded waits.
* Absolute locators.
* Storing credentials in code.
* Running large regression suites sequentially.

---

# Troubleshooting

## Browser Not Found

```bash
playwright install
```

---

## Allure Command Not Found

Verify installation:

```bash
allure --version
```

Reinstall if necessary.

---

## Trace Viewer Not Opening

Verify trace file exists:

```bash
traces/trace.zip
```

Open manually:

```bash
playwright show-trace traces/trace.zip
```

---

# Framework Benefits

This framework provides:

✅ Automated Browser Testing

✅ Rich Allure Reporting

✅ Failure Screenshots

✅ Execution Videos

✅ Playwright Trace Viewer

✅ Network Monitoring

✅ DOM Snapshots

✅ Browser Timeline

✅ Execution Logs

✅ Test Audit Trail

✅ CI/CD Integration Ready

✅ Enterprise-Level Traceability

---

# Conclusion

By combining Playwright, Pytest, Allure, screenshots, videos, and trace files, this framework delivers a complete end-to-end automation solution suitable for enterprise-scale test execution, debugging, reporting, and auditability.
