from selenium.webdriver.common.by import By
from tests.pages.base import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_CONTAINER = (By.CSS_SELECTOR, "h3[data-test='error']")
    TITLE = (By.CLASS_NAME, "app_logo")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.send_keys(self.USERNAME, username)
        self.send_keys(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
    
    def wait_for_page_to_load(self):
        self.find_element(self.USERNAME)
        self.find_element(self.PASSWORD)
        self.find_element(self.LOGIN_BUTTON)