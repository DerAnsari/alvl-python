import requests

base_URL = "https://pokeapi.co/api/v2"

def getPokemonInfo(name):
    url = f"{base_URL}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemonData = response.json()
        return pokemonData
    else:
        print(f"Error, {response.status_code}")

pokemonName = input("enter name of desired pokemon")
pokemonVal = getPokemonInfo(pokemonName)
if pokemonVal: 
    print(pokemonVal["name"],pokemonVal["id"])
