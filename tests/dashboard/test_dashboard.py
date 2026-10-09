import json
from pathlib import Path
import re

from src.fixtures.base import expect, test
from src.pages.InventoryPage import InventoryPage
from src.pages.LoginPage import LoginPage
from src.pages.PIMPage import PIMPage


DATA_FILE = Path(__file__).resolve().parents[2] / "testdata" / "login_user.json"
TEST_DATA = json.loads(DATA_FILE.read_text(encoding="utf-8"))


def _login(page) -> InventoryPage:
    login_page = LoginPage(page)
    dashboard_page = InventoryPage(page)
    user = TEST_DATA["valid_user"]

    login_page.goto()
    login_page.login(user["username"], user["password"])
    dashboard_page.wait_for_load()
    return dashboard_page


def test_dashboard_loads_after_valid_login(test) -> None:
    dashboard_page = _login(test)

    expect(dashboard_page.dashboard_heading).to_be_visible()
    expect(test).to_have_url(dashboard_page.URL)


def test_admin_navigation_is_visible(test) -> None:
    dashboard_page = _login(test)

    expect(dashboard_page.admin_link).to_be_visible()


def test_pim_navigation_opens_pim_page(test) -> None:
    dashboard_page = _login(test)

    dashboard_page.open_pim()

    expect(test).to_have_url(re.compile(r".*/pim/.*"))
    expect(PIMPage(test).page_heading).to_be_visible()


def test_unauthenticated_dashboard_access_redirects_to_login(test) -> None:
    dashboard_page = InventoryPage(test)
    login_page = LoginPage(test)

    dashboard_page.goto()

    expect(test).to_have_url(re.compile(r".*/auth/login"))
    expect(login_page.login_button).to_be_visible()
