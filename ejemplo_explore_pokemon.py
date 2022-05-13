import requests


def print_restul(json_respnse):
    pokemones = json_respnse.get("results")
    for pokemon in pokemones:
        # print(pokemon)
        explore_pokemon(pokemon)

def explore_pokemon(pokemon):
    url_pokemon = pokemon.get("url")
    r = requests.get(url_pokemon)
    json_respnse = r.json()
    # print(json_respnse.keys())
    print("la altura del pokemon {} es de {}".format(pokemon.get("name"), json_respnse.get("height")))

if __name__ == "__main__":
    url = 'http://pokeapi.co/api/v2/pokemon'
    r = requests.get(url)
    json_respnse = r.json()
    print_restul(json_respnse)

    for _ in range(10):
        print("== nuevo ciclo for === ")
        url_next = json_respnse.get("next")
        r = requests.get(url_next)
        json_respnse = r.json()
        print_restul(json_respnse)
