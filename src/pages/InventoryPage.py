from playwright.sync_api import Page

from src.pages.base_page import BasePage


class InventoryPage(BasePage):
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.dashboard_heading = page.get_by_role("heading", name="Dashboard")
        self.admin_link = page.get_by_role("link", name="Admin")

    def goto(self) -> None:
        self.page.goto(self.URL, wait_until="domcontentloaded")
        self.wait_for_ready()
