from playwright.sync_api import Page

from config.settings import settings
from src.pages.base_page import BasePage


class LoginPage(BasePage):
    URL = settings.login_url

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.username = page.get_by_role("textbox", name="Username")
        self.password = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

    def goto(self) -> None:
        self.page.goto(self.URL, wait_until="load", timeout=60000)
        self.wait_for_ready()

    def login(self, username: str, password: str) -> None:
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def get_error_message(self):
        return self.page.get_by_text("Invalid credentials")

    def is_username_valid(self) -> bool:
        return self.username.evaluate("element => element.validity.valid")

    def is_password_valid(self) -> bool:
        return self.password.evaluate("element => element.validity.valid")
