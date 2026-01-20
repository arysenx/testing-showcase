import pytest
import requests

@pytest.fixture(scope="session")
def api_base_url(parse_config):
    return parse_config("[CONF:apis.pokemon.base_url]")

@pytest.fixture(scope="function")
def api_client(api_base_url):
    session = requests.Session()
    yield session
    session.close()
