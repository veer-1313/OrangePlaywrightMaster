import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def test(page: Page):
    yield page


__all__ = ["test", "expect"]
