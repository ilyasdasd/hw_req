
import requests
import json

heroes_list = ['Hulk', 'Captain america', 'Thanos']

intelligence_dict = {'Hulk': 0, 'Captain america': 0, 'Thanos': 0}
url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/'

for hero in heroes_list:
    hero_dict = json.loads(requests.get(url + hero).content())
    intelligence_dict[hero] = int(hero_dict['results'][0]['powerstats']['intelligence'])




