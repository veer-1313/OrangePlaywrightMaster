from playwright.sync_api import Page

# Test file is added to the repo to demonstrate how to use the BasePage class and its subclasses. It is not part of the actual application code.

class BasePage:
    def __init__(self, page: Page) -> None:
        self.page: Page = page

    def goto(self) -> None:
        """Abstract method - must be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement goto()")

    def wait_for_ready(self) -> None:
        """Wait until the page has fully loaded and the app shell is ready."""
        self.page.wait_for_load_state("load")
