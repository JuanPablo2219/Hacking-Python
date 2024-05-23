import requests
import argparse


def dats_pokemos(name: str):
    url = f'https://pokeapi.co/api/v2/pokemon/{name}'
    response = requests.get(url)

    try:
        if response.status_code == 200:
         data =  response.json()
        print(data ['abilities'])
    except:        
        print(f'Error', {response.status_code})

parser = argparse.ArgumentParser()
parser.add_argument('Name_pokemon', type=str, default='pikachu')

arg = parser.parse_args()

dats_pokemos(arg.Name_pokemon)