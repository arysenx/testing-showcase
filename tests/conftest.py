import pytest
import yaml
from pathlib import Path
from .common.helpers import parse_config_value

@pytest.fixture(scope="session")
def config_data():
    config_path = Path(__file__).parent.parent / 'config.yml'
    if not config_path.exists():
        pytest.fail(f"Config file not found at {config_path}")
        
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session")
def parse_config(config_data):
    return lambda value: parse_config_value(value, config_data)

def pytest_addoption(parser):
    parser.addoption(
        "--headless", action="store_true", default=False, help="Run browser in headless mode"
    )

