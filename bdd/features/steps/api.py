import json
from behave import step
from jsonschema import validate
from pathlib import Path


@step('the API base URL is "{base_url}"')
def set_api_base_url(context, base_url):
    base_url = context.parse_config(base_url)
    context.api_base_url = base_url
    context.response = None


@step('send GET request to "{endpoint}"')
def send_get_request(context, endpoint):
    endpoint = context.parse_config(endpoint)
    url = context.api_base_url + endpoint
    context.response = context.session.get(url)


@step('send POST request to "{endpoint}" with body')
def send_post_request_with_body(context, endpoint):
    endpoint = context.parse_config(endpoint)
    url = context.api_base_url + endpoint
    body = json.loads(context.text)
    context.response = context.session.post(url, json=body)


@step('response status code is {status_code:d}')
def check_response_status_code(context, status_code):
    assert context.response.status_code == status_code, \
        f"Expected status code {status_code} but got {context.response.status_code}"


@step('response body has "{field}" equal to "{value}"')
def check_response_field(context, field, value):
    value = context.parse_config(value)
    response_json = context.response.json()
    
    fields = field.split('.')
    actual_value = response_json
    for f in fields:
        actual_value = actual_value[f]
    
    assert str(actual_value) == value, \
        f"Expected {field} to be '{value}' but got '{actual_value}'"


@step('response body follows JSON schema "{schema_file}"')
def check_response_schema(context, schema_file):
    schema_file = context.parse_config(schema_file)
    schema_path = Path(__file__).parent.parent / 'schemas' / schema_file
    
    with open(schema_path, 'r') as f:
        schema = json.load(f)
    
    validate(instance=context.response.json(), schema=schema)

