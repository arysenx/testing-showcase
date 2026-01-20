import pytest
import importlib
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver(config_data, request):
    """Initializes Chrome driver for UI tests."""

    from selenium.webdriver.chrome.options import Options
    
    chrome_options = Options()
    if request.config.getoption("--headless"):
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    
    timeout = config_data.get('environment', {}).get('timeout', 10)
    driver.implicitly_wait(timeout)
    
    yield driver
    
    driver.quit()

@pytest.fixture(scope="function")
def page_loader(driver):
    """Factory fixture to load page objects by name."""
    def _load_page(page_name):
        base_name = page_name.replace('_page', '')
        # Convert snake_case to PascalCase + 'Page'
        class_name = ''.join(word.capitalize() for word in base_name.split('_')) + 'Page'
        
        try:
            # Assumes page objects are in tests.pages package
            module = importlib.import_module(f'tests.pages.{base_name}')
            page_class = getattr(module, class_name)
            return page_class(driver)
        except (ImportError, AttributeError) as e:
            pytest.fail(f"Could not load page object for '{page_name}': {e}")
            
    return _load_page
