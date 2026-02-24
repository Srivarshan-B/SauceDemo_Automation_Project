from utils.api_utils import APIUtils
from utils.config_reader import ConfigReader


def test_api_products():
    config = ConfigReader()
    api = APIUtils(config.get("api_base_url"))

    response = api.get_products()
    assert response.status_code == 200