import logging
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = PROJECT_ROOT / "Log"
LOG_FILE = LOG_DIR / "automation.log"


def get_logger(name: str = "playwright_automation") -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    LOG_DIR.mkdir(exist_ok=True)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
    logger.addHandler(handler)
    logger.propagate = False
    return logger