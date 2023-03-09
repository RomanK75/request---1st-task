import requests
from pprint import pprint

def req(heroe_list = ['Hulk','Captain America','Thanos']):
    adres = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url = adres, timeout=5)
    all_heroes = response.json()
    searched_hero = {'name':'', 'intelligence': 0}
    for heroe in all_heroes:
        if heroe['name'] in heroe_list:
            if heroe['powerstats']['intelligence'] > searched_hero['intelligence']:
                searched_hero['name'], searched_hero['intelligence'] = heroe['name'], heroe['powerstats']['intelligence']
    pprint(searched_hero)

if __name__ == '__main__':
    req()