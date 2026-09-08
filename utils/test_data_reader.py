import json
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_json(file_name: str) -> Any:
    """Load a JSON file from the project testdata directory."""
    data_file = PROJECT_ROOT / "testdata" / file_name
    with data_file.open(encoding="utf-8") as file:
        return json.load(file)
