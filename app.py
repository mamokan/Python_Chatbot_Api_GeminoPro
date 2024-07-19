import requests
base_url="https://pokeapi.co/api/v2/pokemon/"
pokemon_name=input("enter pokemon name:")
def get_pokemon_data():
    response = requests.get(f"{base_url}/{pokemon_name}")
    if response.status_code == 200:
        data=response.json()
        print("Pokemon name: ", data["name"])
        print("Pokemon height: ", data["height"])
        print("Pokemon weight: ", data["weight"])
        
    else:
        return "no data available"
get_pokemon_data()