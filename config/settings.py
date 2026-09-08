import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")


@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv(
        "BASE_URL",
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
    )
    browser: str = os.getenv("BROWSER", "chrome").lower()
    headless: bool = os.getenv("HEADLESS", "false").lower() == "true"
    implicit_wait: int = int(os.getenv("IMPLICIT_WAIT", "0"))
    explicit_wait: int = int(os.getenv("EXPLICIT_WAIT", "15"))


settings = Settings()
