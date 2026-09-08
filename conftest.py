import pytest
from playwright.sync_api import Page, sync_playwright

from config.artifacts import capture_failure
from config.logger import get_logger
from config.settings import settings


LOGGER = get_logger()

try:
    import allure
except ImportError:
    allure = None


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--browser-name",
        action="store",
        default=settings.browser,
        choices=("chrome", "firefox"),
        help="Browser used for UI tests.",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=settings.headless,
        help="Run the browser without opening a window.",
    )


@pytest.fixture
def page(request: pytest.FixtureRequest) -> Page:
    browser = request.config.getoption("--browser-name")
    headless = request.config.getoption("--headless")

    with sync_playwright() as playwright:
        browser_type = getattr(playwright, "chromium" if browser == "chrome" else browser)
        test_browser = browser_type.launch(
            headless=headless,
            args=["--disable-http2"],
        )
        context = test_browser.new_context(viewport={"width": 1920, "height": 1080})
        test_page = context.new_page()
        test_page.set_default_timeout(settings.explicit_wait * 1000)
        yield test_page
        context.close()
        test_browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        if report.passed:
            LOGGER.info("PASSED: %s", item.nodeid)
        else:
            LOGGER.error("FAILED: %s", item.nodeid)
            page = item.funcargs.get("page") or item.funcargs.get("authenticated_page")
            if page is not None:
                try:
                    screenshot_path = capture_failure(page, item.nodeid)
                    LOGGER.info("Failure screenshot: %s", screenshot_path)
                    if allure is not None:
                        allure.attach.file(
                            str(screenshot_path),
                            name="failure-screenshot",
                            attachment_type=allure.attachment_type.PNG,
                        )
                except Exception as screenshot_error:
                    LOGGER.exception("Could not capture failure screenshot: %s", screenshot_error)
