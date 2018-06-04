import json
from sys import stdout
import dota2api
from dota2api.src.exceptions import APIAuthenticationError, APIError

# API key can be found here https://steamcommunity.com/dev/apikey
api_key = "78AB51DECA9BAA091DC09D0FEFED65EE"

# random recent match ID to start collecting information from in descending order
latest_match_id = 3933473953

# desired size of data set
data_size = 100

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

