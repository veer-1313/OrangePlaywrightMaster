import json
from pathlib import Path

from src.fixtures.base import expect, test
from src.pages.InventoryPage import InventoryPage
from src.pages.LoginPage import LoginPage
from src.pages.SystemUsersPage import SystemUsersPage

DATA_FILE = Path(__file__).resolve().parents[2] / "testdata" / "login_user.json"
TEST_DATA = json.loads(DATA_FILE.read_text(encoding="utf-8"))


def test_system_users_page_loads(test) -> None:
    login_page = LoginPage(test)
    inventory_page = InventoryPage(test)
    system_users_page = SystemUsersPage(test)
    user = TEST_DATA["valid_user"]

    login_page.goto()
    login_page.login(user["username"], user["password"])

    expect(inventory_page.admin_link).to_be_visible()

    system_users_page.goto()
    expect(system_users_page.page_heading).to_be_visible()
    expect(system_users_page.add_button).to_be_visible()
    expect(system_users_page.records_found).to_be_visible()


def test_system_users_add_form_validation(test) -> None:
    login_page = LoginPage(test)
    system_users_page = SystemUsersPage(test)
    user = TEST_DATA["valid_user"]

    login_page.goto()
    login_page.login(user["username"], user["password"])

    system_users_page.goto()
    system_users_page.open_add_form()
    system_users_page.submit_form()

    expect(test.get_by_role("heading", name="Add User")).to_be_visible()
    expect(test.get_by_text("Required").first).to_be_visible()


def test_system_users_search_unknown_username_shows_empty_state(test) -> None:
    login_page = LoginPage(test)
    system_users_page = SystemUsersPage(test)
    user = TEST_DATA["valid_user"]

    login_page.goto()
    login_page.login(user["username"], user["password"])
    system_users_page.goto()
    system_users_page.search_by_username("NoSuchSystemUser123")

    expect(test.get_by_text("No Records Found")).to_be_visible()
