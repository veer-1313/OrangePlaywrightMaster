from playwright.sync_api import Page

from config.settings import settings
from src.pages.base_page import BasePage


class InventoryPage(BasePage):
    URL = settings.dashboard_url

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.dashboard_heading = page.get_by_role("heading", name="Dashboard")
        self.admin_link = page.get_by_role("link", name="Admin")
        self.pim_link = page.get_by_role("link", name="PIM")

    def goto(self) -> None:
        self.page.goto(self.URL, wait_until="load", timeout=60000)
        self.wait_for_ready()

    def open_pim(self) -> None:
        self.pim_link.click()

    def open_admin(self) -> None:
        self.admin_link.click()

    def wait_for_load(self) -> None:
        self.dashboard_heading.wait_for(state="visible")
