import json
from pathlib import Path

from playwright.sync_api import Page

from src.fixtures.base import expect, test
from src.pages.InventoryPage import InventoryPage
from src.pages.LoginPage import LoginPage


USERS_FILE = Path(__file__).parents[1] / "data" / "users.json"
users = json.loads(USERS_FILE.read_text(encoding="utf-8"))


def test_standard_login(test: Page) -> None:
    login_page = LoginPage(test)
    dashboard = InventoryPage(test)

    login_page.goto()
    login_page.login(**users["standard"])

    expect(dashboard.dashboard_heading).to_be_visible()
    expect(test).to_have_url(dashboard.URL)
    expect(dashboard.admin_link).to_be_visible()
