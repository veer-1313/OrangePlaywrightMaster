from api.client import ApiClient
from api.settings import API_BASE_URL


def test_api_client_can_read_json() -> None:
    response = ApiClient(API_BASE_URL).get("/json")

    assert response.ok
    assert response.headers["content-type"].startswith("application/json")