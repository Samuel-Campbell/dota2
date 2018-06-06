import json
from sys import stdout
import dota2api
from dota2api.src.exceptions import APIAuthenticationError, APIError
import time
from scrape_dota_buff import scrape


# API key can be found here https://steamcommunity.com/dev/apikey
api_key = "78AB51DECA9BAA091DC09D0FEFED65EE"

# random recent match ID to start collecting information from in descending order
latest_match_id = 3933473953

# desired size of data set
data_size = 1000

"""
try:
    # init key from environment variables
    api = dota2api.Initialise()

except APIAuthenticationError:
    # init key from api_key variable
    api = dota2api.Initialise(api_key=api_key)

match_dict = {}
heroes_dict = api.get_heroes()
items_dict = api.get_game_items()

original_data_size = data_size * 1.0

while data_size > 0:
    latest_match_id = latest_match_id - 1

    percent = 100.0 - ((data_size / original_data_size) * 100)
    stdout.write("\r[+] Data Collected (percent): %f " % percent)
    stdout.flush()

    # Practice matches cannot be queried. If they are then an error is thrown
    try:
        match = api.get_match_details(match_id=latest_match_id)
        match_dict[latest_match_id] = match
        data_size -= 1
    except APIError:
        pass

"""
player_stats = {}

with open('data/match.json') as fp:
    match_dict = json.load(fp)

i = 0
print()
for key in match_dict:
    player_list = match_dict[key]['players']
    for player in player_list:
        time.sleep(0.01)
        try:
            account_id = player['account_id']
            player_info = scrape(account_id)
            player_stats[account_id] = player_info

            percent = (i / (data_size * 10)) * 100
            stdout.write("\r[+] Data Scraped (percent): %f " % percent)
            stdout.flush()

            i += 1

        except KeyError:
            pass

"""        
# save match data
print("\n[+] Saving match data")
with open('data/match.json', 'w') as fp:
    json.dump(match_dict, fp)

# save heroes data
print("[+] Saving heroes data")
with open('data/heroes.json', 'w') as fp:
    json.dump(heroes_dict, fp)

# save items data
print("[+] Saving items data")
with open('data/items.json', 'w') as fp:
    json.dump(items_dict, fp)
"""

# save player stats
print("[+] Saving player stats")
with open('data/player_stats.json', 'w') as fp:
    json.dump(player_stats, fp)
