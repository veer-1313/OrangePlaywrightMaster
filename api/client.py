from dataclasses import dataclass
from typing import Any

import requests


@dataclass
class ApiClient:
    base_url: str
    timeout: int = 30

    def get(self, path: str, **kwargs: Any) -> requests.Response:
        return requests.get(
            f"{self.base_url.rstrip('/')}/{path.lstrip('/')}",
            timeout=self.timeout,
            **kwargs,
        )

    def post(self, path: str, **kwargs: Any) -> requests.Response:
        return requests.post(
            f"{self.base_url.rstrip('/')}/{path.lstrip('/')}",
            timeout=self.timeout,
            **kwargs,
        )