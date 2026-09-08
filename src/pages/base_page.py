from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page: Page = page

    def goto(self) -> None:
        """Abstract method - must be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement goto()")

    def wait_for_ready(self) -> None:
        """Wait until the DOM is fully loaded."""
        self.page.wait_for_load_state("domcontentloaded")
