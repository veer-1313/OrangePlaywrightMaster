import re

from playwright.sync_api import Page, expect

from src.pages.base_page import BasePage


class PIMPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page_heading = page.get_by_role("heading", name="PIM")
        self.employee_information_heading = page.get_by_role("heading", name="Employee Information")
        self.employee_name_input = page.get_by_label("Employee Name")
        self.employee_id_input = page.get_by_label("Employee Id")
        self.search_button = page.get_by_role("button", name="Search")
        self.reset_button = page.get_by_role("button", name="Reset")
        self.add_button = page.get_by_role("button", name="Add")
        self.save_button = page.get_by_role("button", name="Save")
        self.table = page.locator(".oxd-table-card")
        self.no_results = page.get_by_text("No Records Found")

    def wait_for_load(self) -> None:
        expect(self.page).to_have_url(re.compile(r".*/pim/.*"))
        expect(self.page_heading).to_be_visible()

    def search_employee_by_name(self, employee_name: str) -> None:
        self.employee_name_input.fill(employee_name)
        self.search_button.click()

    def search_employee_by_id(self, employee_id: str) -> None:
        self.employee_id_input.fill(employee_id)
        self.search_button.click()

    def reset_search(self) -> None:
        self.reset_button.click()

    def open_add_form(self) -> None:
        self.add_button.click()

    def submit_employee_form(self) -> None:
        self.save_button.click()

    def open_employee(self, employee_name: str) -> None:
        self.table.filter(has_text=employee_name).first.click()

    def get_visible_employee_names(self) -> list[str]:
        rows = self.table.all_inner_texts()
        return [text for text in rows if text.strip()]

    def employee_displayed(self, employee_name: str) -> bool:
        return employee_name in self.page.locator("body").inner_text()
