from playwright.sync_api import Page

from src.pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.username = page.get_by_role("textbox", name="Username")
        self.password = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

    def goto(self) -> None:
        self.page.goto(self.URL, wait_until="domcontentloaded")
        self.wait_for_ready()

    def login(self, username: str, password: str) -> None:
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
