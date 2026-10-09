import json
import re
from pathlib import Path

from src.fixtures.base import expect, test
from src.pages.InventoryPage import InventoryPage
from src.pages.LoginPage import LoginPage
from src.pages.PIMPage import PIMPage

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "users.json"
PIM_DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "pim_test_data.json"
USER_DATA = json.loads(DATA_FILE.read_text(encoding="utf-8"))
PIM_DATA = json.loads(PIM_DATA_FILE.read_text(encoding="utf-8"))


def _login_and_open_pim(page) -> PIMPage:
    login_page = LoginPage(page)
    dashboard_page = InventoryPage(page)
    user = USER_DATA["standard"]

    login_page.goto()
    login_page.login(user["username"], user["password"])

    expect(dashboard_page.dashboard_heading).to_be_visible()
    dashboard_page.open_pim()

    pim_page = PIMPage(page)
    pim_page.wait_for_load()
    return pim_page


def test_pim_page_is_visible_after_login(test) -> None:
    login_page = LoginPage(test)
    dashboard_page = InventoryPage(test)
    user = USER_DATA["standard"]

    login_page.goto()
    login_page.login(user["username"], user["password"])

    expect(dashboard_page.dashboard_heading).to_be_visible()
    expect(dashboard_page.pim_link).to_be_visible()

    dashboard_page.open_pim()

    expect(test).to_have_url(re.compile(r".*/pim/.*"))
    expect(test.get_by_role("heading", name="PIM")).to_be_visible()


def test_search_employee_by_valid_name(test) -> None:
    pim_page = _login_and_open_pim(test)

    valid_name = "Aaliyah Haq"
    pim_page.search_employee_by_name(valid_name)

    expect(test.get_by_text(valid_name)).to_be_visible()
    expect(test).to_have_url(re.compile(r".*/pim/.*"))


def test_search_employee_by_valid_id(test) -> None:
    pim_page = _login_and_open_pim(test)

    valid_id = "0001"
    pim_page.search_employee_by_id(valid_id)

    expect(test.get_by_text(valid_id)).to_be_visible()
    expect(test).to_have_url(re.compile(r".*/pim/.*"))


def test_invalid_employee_search_shows_no_records(test) -> None:
    pim_page = _login_and_open_pim(test)
    invalid_name = PIM_DATA["search"]["invalid_name"]

    pim_page.search_employee_by_name(invalid_name)

    expect(test.get_by_text("No Records Found")).to_be_visible()
    expect(test).to_have_url(re.compile(r".*/pim/.*"))


def test_add_employee_form_validation(test) -> None:
    pim_page = _login_and_open_pim(test)

    pim_page.open_add_form()
    expect(test.get_by_role("heading", name="Add Employee")).to_be_visible()

    pim_page.submit_employee_form()

    expect(test.get_by_text("Required").first).to_be_visible()


def test_reset_employee_search_restores_list(test) -> None:
    pim_page = _login_and_open_pim(test)

    pim_page.search_employee_by_name("Aaliyah Haq")
    expect(test.get_by_text("Aaliyah Haq")).to_be_visible()

    pim_page.reset_search()

    expect(pim_page.table.first).to_be_visible()
    expect(test).to_have_url(re.compile(r".*/pim/.*"))
