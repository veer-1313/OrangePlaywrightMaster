import re
from pathlib import Path

from playwright.sync_api import Page


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCREENSHOT_DIR = PROJECT_ROOT / "Screenshot"


def safe_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("_")


def capture_failure(page: Page, test_name: str) -> Path:
    SCREENSHOT_DIR.mkdir(exist_ok=True)
    screenshot_path = SCREENSHOT_DIR / f"{safe_name(test_name)}.png"
    page.screenshot(path=str(screenshot_path), full_page=True)
    return screenshot_path