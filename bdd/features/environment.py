# features/environment.py
import importlib
import yaml
import sys
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path


def get_page_object(context, page_name):
    base_name = page_name.replace('_page', '')
    class_name = ''.join(word.capitalize() for word in base_name.split('_')) + 'Page'
    
    try:
        module = importlib.import_module(f'bdd.pages.{base_name}')
        page_class = getattr(module, class_name)
        return page_class(context.driver)
    except (ImportError, AttributeError) as e:
        raise ValueError(f"Could not load page object for '{page_name}': {e}")


def parse_config_value(value, config_data):
    if isinstance(value, str) and value.startswith('[CONF:') and value.endswith(']'):
        keys = value[6:-1].split('.')
        result = config_data
        for key in keys:
            result = result[key]
        return result
    return value


def before_all(context):
    config_path = Path(__file__).parent.parent.parent / 'config.yml'
    with open(config_path, 'r') as f:
        context.config_data = yaml.safe_load(f)
    
    context.get_page_object = lambda page_name: get_page_object(context, page_name)
    context.parse_config = lambda value: parse_config_value(value, context.config_data)


def before_scenario(context, scenario):
    if 'web' in scenario.tags:
        context.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        context.driver.maximize_window()
        context.driver.implicitly_wait(context.config_data['environment']['timeout'])
    
    if 'api' in scenario.tags:
        context.session = requests.Session()
        

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()
    if hasattr(context, 'session'):
        context.session.close()