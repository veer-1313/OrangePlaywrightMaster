import os
from configparser import ConfigParser
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")

CONFIG_PATH = PROJECT_ROOT / "config" / "config.ini"
CONFIG = ConfigParser()
CONFIG.read(CONFIG_PATH, encoding="utf-8")


def _get_config_value(section: str, key: str, default: str) -> str:
    if CONFIG.has_section(section) and CONFIG.has_option(section, key):
        value = CONFIG.get(section, key).strip()
        if value:
            return value
    return default


def _build_url(base_url: str, path: str) -> str:
    normalized_base = base_url.rstrip("/")
    normalized_path = path if path.startswith("/") else f"/{path}"
    return f"{normalized_base}{normalized_path}"


@dataclass(frozen=True)
class Settings:
    base_url: str = _get_config_value("app", "base_url", "https://opensource-demo.orangehrmlive.com/web/index.php")
    login_url: str = _build_url(
        _get_config_value("app", "base_url", "https://opensource-demo.orangehrmlive.com/web/index.php"),
        _get_config_value("app", "login_path", "/auth/login"),
    )
    dashboard_url: str = _build_url(
        _get_config_value("app", "base_url", "https://opensource-demo.orangehrmlive.com/web/index.php"),
        _get_config_value("app", "dashboard_path", "/dashboard/index"),
    )
    system_users_url: str = _build_url(
        _get_config_value("app", "base_url", "https://opensource-demo.orangehrmlive.com/web/index.php"),
        _get_config_value("app", "system_users_path", "/admin/viewSystemUsers"),
    )
    browser: str = os.getenv("BROWSER", "chrome").lower()
    headless: bool = os.getenv("HEADLESS", "false").lower() == "true"
    implicit_wait: int = int(os.getenv("IMPLICIT_WAIT", "0"))
    explicit_wait: int = int(os.getenv("EXPLICIT_WAIT", "60"))


settings = Settings()
