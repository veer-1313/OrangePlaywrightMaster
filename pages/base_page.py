from playwright.sync_api import Locator, Page

from config.settings import settings


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self, url: str) -> None:
        self.page.goto(url, wait_until="domcontentloaded")

    def wait_for_visible(self, locator: str) -> Locator:
        element = self.page.locator(locator)
        element.wait_for(state="visible")
        return element

    def click(self, locator: str) -> None:
        self.page.locator(locator).click()

    def type_text(self, locator: str, text: str) -> None:
        self.page.locator(locator).fill(text)
