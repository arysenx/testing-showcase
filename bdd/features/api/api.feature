Feature: Pokemon API test

@api
Scenario: Get Pokemon by name - Pokemon found
    Given the API base URL is "https://pokeapi.co/api/v2"
     When send GET request to "/pokemon/pikachu"
     Then response status code is 200
     And response body has "name" equal to "pikachu"

@api
Scenario: Get Pokemon by name - Response body has expected data
    Given the API base URL is "https://pokeapi.co/api/v2"
     When send GET request to "/pokemon/pikachu"
     Then response status code is 200
     And response body follows JSON schema "pokemon_api_response.json"

@api
Scenario: Get Pokemon by id - Pokemon found
    Given the API base URL is "https://pokeapi.co/api/v2"
     When send GET request to "/pokemon/25"
     Then response status code is 200
     And response body has "name" equal to "pikachu"

@api
Scenario: Get Pokemon by name - Pokemon not found
    Given the API base URL is "https://pokeapi.co/api/v2"
     When send GET request to "/pokemon/invalid"
     Then response status code is 404

@api
Scenario: Get Pokemon by id - Pokemon not found
    Given the API base URL is "https://pokeapi.co/api/v2"
     When send GET request to "/pokemon/999999"
     Then response status code is 404