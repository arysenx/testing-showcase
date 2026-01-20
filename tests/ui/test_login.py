import pytest

@pytest.mark.ui
def test_login_successful(driver, page_loader, parse_config):
    url = parse_config("[CONF:pages.saucedemo.url]")
    driver.get(url)
    
    login_page = page_loader("login_page")
    login_page.wait_for_page_to_load()
    
    username = parse_config("[CONF:users.success.username]")
    login_page.send_keys(login_page.USERNAME, username)
    
    password = parse_config("[CONF:users.success.password]")
    login_page.send_keys(login_page.PASSWORD, password)
    
    login_page.click(login_page.LOGIN_BUTTON)
    
    actual_text = login_page.get_text(login_page.TITLE)
    assert "Swag Labs" in actual_text

@pytest.mark.ui
def test_login_failed(driver, page_loader, parse_config):
    url = parse_config("[CONF:pages.saucedemo.url]")
    driver.get(url)
    
    login_page = page_loader("login_page")
    login_page.wait_for_page_to_load()
    
    username = parse_config("[CONF:users.failure.username]")
    login_page.send_keys(login_page.USERNAME, username)
    
    password = parse_config("[CONF:users.failure.password]")
    login_page.send_keys(login_page.PASSWORD, password)
    
    login_page.click(login_page.LOGIN_BUTTON)
    
    assert login_page.is_visible(login_page.ERROR_CONTAINER), "Error container should be visible"
    assert login_page.is_visible(login_page.ERROR_CONTAINER), "Error container should be visible"
    
    error_text = login_page.get_text(login_page.ERROR_CONTAINER)
    expected_text = "Epic sadface: Username and password do not match any user in this service"
    assert expected_text in error_text, f"Expected '{expected_text}' to be in '{error_text}'"
