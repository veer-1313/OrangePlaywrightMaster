import pytest
from playwright.sync_api import Page, expect


@pytest.mark.smoke
def test_saucedemo_login_page_loads(page: Page) -> None:
    # Navigate to the SauceDemo login page
    page.goto("https://www.saucedemo.com")

    # Assert that the Username and Password fields are visible
    expect(page.get_by_role("textbox", name="Username")).to_be_visible()
    expect(page.get_by_role("textbox", name="Password")).to_be_visible()
