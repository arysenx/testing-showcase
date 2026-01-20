import pytest
import json
from pathlib import Path
from jsonschema import validate

@pytest.mark.api
def test_get_pokemon_by_name_found(api_client, api_base_url):
    response = api_client.get(f"{api_base_url}/pokemon/pikachu")
    assert response.status_code == 200
    assert response.json()['name'] == 'pikachu'

@pytest.mark.api
def test_get_pokemon_schema_validation(api_client, api_base_url):
    response = api_client.get(f"{api_base_url}/pokemon/pikachu")
    assert response.status_code == 200
    
    schema_path = Path(__file__).parent.parent / 'common' / 'schemas' / 'pokemon_api_response.json'
    with open(schema_path, 'r') as f:
        schema = json.load(f)
    
    validate(instance=response.json(), schema=schema)

@pytest.mark.api
def test_get_pokemon_by_id_found(api_client, api_base_url):
    response = api_client.get(f"{api_base_url}/pokemon/25")
    assert response.status_code == 200
    assert response.json()['name'] == 'pikachu'

@pytest.mark.api
def test_get_pokemon_by_name_not_found(api_client, api_base_url):
    response = api_client.get(f"{api_base_url}/pokemon/invalid")
    assert response.status_code == 404

@pytest.mark.api
def test_get_pokemon_by_id_not_found(api_client, api_base_url):
    response = api_client.get(f"{api_base_url}/pokemon/999999")
    assert response.status_code == 404
