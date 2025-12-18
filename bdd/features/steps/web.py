from behave import step


@step('the "{page_name}" page is loaded')
def page_is_loaded(context, page_name):
    page_name = context.parse_config(page_name)
    context.page = context.get_page_object(page_name)
    if not context.page:
        raise Exception(f"Page '{page_name}' not found")
    context.page.wait_for_page_to_load()


@step('user goes to "{url}"')
def go_to_webpage(context, url):
    url = context.parse_config(url)
    context.driver.get(url)


@step('write "{text}" into "{field_name}" field')
def type_text_into_element(context, text, field_name):
    text = context.parse_config(text)
    field_name = context.parse_config(field_name)
    locator = getattr(context.page, field_name.upper(), None)
    if locator:
        context.page.send_keys(locator, text)
    else:
        raise AttributeError(f"Locator '{field_name}' not found in {context.page.__class__.__name__}")


@step('click on "{button_name}" button')
def click_button(context, button_name):
    button_name = context.parse_config(button_name)
    locator = getattr(context.page, button_name.upper(), None)
    if locator:
        context.page.click(locator)
    else:
        raise AttributeError(f"Locator '{button_name}' not found in {context.page.__class__.__name__}")


@step('click on "{link_name}" link')
def click_link(context, link_name):
    link_name = context.parse_config(link_name)
    locator = getattr(context.page, link_name.upper(), None)
    if locator:
        context.page.click(locator)
    else:
        raise AttributeError(f"Locator '{link_name}' not found in {context.page.__class__.__name__}")


@step('"{element_name}" element is visible')
def element_is_visible(context, element_name):
    element_name = context.parse_config(element_name)
    locator = getattr(context.page, element_name.upper(), None)
    if locator:
        assert context.page.is_visible(locator), f"Element '{element_name}' is not visible"
    else:
        raise AttributeError(f"Locator '{element_name}' not found in {context.page.__class__.__name__}")


@step('"{element_name}" element has "{expected_text}" text')
def element_has_text(context, element_name, expected_text):
    element_name = context.parse_config(element_name)
    expected_text = context.parse_config(expected_text)
    locator = getattr(context.page, element_name.upper(), None)
    if locator:
        actual_text = context.page.get_text(locator)
        assert expected_text in actual_text, f"Expected '{expected_text}' but got '{actual_text}'"
    else:
        raise AttributeError(f"Locator '{element_name}' not found in {context.page.__class__.__name__}")