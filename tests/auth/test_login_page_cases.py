import json
from pathlib import Path

from src.fixtures.base import expect, test
from src.pages.InventoryPage import InventoryPage
from src.pages.LoginPage import LoginPage

DATA_FILE = Path(__file__).resolve().parents[2] / "testdata" / "login_user.json"
TEST_DATA = json.loads(DATA_FILE.read_text(encoding="utf-8"))


def test_login_success_with_valid_data(test) -> None:
    login_page = LoginPage(test)
    dashboard_page = InventoryPage(test)
    user = TEST_DATA["valid_user"]

    login_page.goto()
    login_page.login(user["username"], user["password"])

    expect(dashboard_page.dashboard_heading).to_be_visible()
    expect(test).to_have_url(dashboard_page.URL)
    expect(dashboard_page.admin_link).to_be_visible()


def test_login_with_invalid_credentials_shows_error(test) -> None:
    login_page = LoginPage(test)
    user = TEST_DATA["invalid_user"]

    login_page.goto()
    login_page.login(user["username"], user["password"])

    expect(login_page.get_error_message()).to_be_visible()
    expect(test).to_have_url(login_page.URL)


def test_login_with_empty_username_and_password_shows_validation(test) -> None:
    login_page = LoginPage(test)

    login_page.goto()
    login_page.login("", "")

    assert not login_page.is_username_valid()
    assert not login_page.is_password_valid()
    expect(test).to_have_url(login_page.URL)


def test_login_with_valid_username_and_empty_password_shows_validation(test) -> None:
    login_page = LoginPage(test)
    user = TEST_DATA["valid_user"]

    login_page.goto()
    login_page.login(user["username"], "")

    assert not login_page.is_password_valid()
    expect(test).to_have_url(login_page.URL)


def test_login_with_empty_username_and_valid_password_shows_validation(test) -> None:
    login_page = LoginPage(test)
    user = TEST_DATA["valid_user"]

    login_page.goto()
    login_page.login("", user["password"])

    assert not login_page.is_username_valid()
    expect(test).to_have_url(login_page.URL)


def test_login_with_valid_username_and_wrong_password_shows_error(test) -> None:
    login_page = LoginPage(test)
    user = TEST_DATA["valid_user"]

    login_page.goto()
    login_page.login(user["username"], "wrong_password")

    expect(login_page.get_error_message()).to_be_visible()
    expect(test).to_have_url(login_page.URL)
