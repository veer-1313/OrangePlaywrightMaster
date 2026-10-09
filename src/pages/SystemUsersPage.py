from playwright.sync_api import Page

from config.settings import settings
from src.pages.base_page import BasePage


class SystemUsersPage(BasePage):
    URL = settings.system_users_url

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page_heading = page.get_by_role("heading", name="System Users")
        self.add_button = page.get_by_role("button", name="Add")
        self.save_button = page.get_by_role("button", name="Save")
        self.reset_button = page.get_by_role("button", name="Reset")
        self.search_button = page.get_by_role("button", name="Search")
        self.records_found = page.locator("text=Records Found")
        self.username_input = page.get_by_label("Username")
        self.employee_name_input = page.get_by_label("Employee Name")
        self.table = page.locator(".oxd-table-card")

    def goto(self) -> None:
        self.page.goto(self.URL, wait_until="load", timeout=60000)
        self.wait_for_ready()

    def open_add_form(self) -> None:
        self.add_button.click()

    def submit_form(self) -> None:
        self.save_button.click()

    def search_by_username(self, username: str) -> None:
        self.username_input.fill(username)
        self.search_button.click()

    def visible_user_rows(self):
        return self.table
