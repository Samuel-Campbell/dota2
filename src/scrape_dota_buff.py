from requests import get
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import requests
requests.packages.urllib3.disable_warnings()


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None
    """
    try:
        resp = get(url, verify=False, headers={'User-agent': 'your bot 0.1'})
        if is_good_response(resp):
            return resp.content
        else:
            print("Bad response")
            return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns true if the response seems to be HTML, false otherwise
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


def scrape_player(player_id):
    try:
        url = "https://www.dotabuff.com/players/" + str(player_id) + "/heroes"
        raw_html = simple_get(url)
        html = BeautifulSoup(raw_html, 'html.parser')
        t = html.select("tbody")[1]
        return_dict = {}

        for hero_tr in t.select("tr"):
            hero_td = hero_tr.select("td")
            hero_name = hero_td[0]['data-value']
            games_played = hero_td[2]['data-value']
            win_ratio = hero_td[3]['data-value']
            kda = hero_td[4]['data-value']

            return_dict[hero_name] = {
                'games_played': games_played,
                'win_ratio': win_ratio,
                'kda': kda
            }

        return return_dict
    except:
        print("Error")
        return None


def scrape_hero_monthly_stats():
    url = "https://www.dotabuff.com/heroes/played"
    raw_html = simple_get(url)
    html = BeautifulSoup(raw_html, 'html.parser')
    t = html.select("tbody")[0]

    hero_information = {}

    for hero_tr in t.select("tr"):
        hero_td = hero_tr.select("td")
        hero_name = hero_td[0]['data-value']
        games_played = hero_td[2]['data-value']
        pick_rate = hero_td[3]['data-value']
        win_ratio = hero_td[4]['data-value']
        kda = hero_td[5]['data-value']

        hero_information[hero_name] = {
            'games_played': games_played,
            'pick_rate': pick_rate,
            'win_ratio': win_ratio,
            'kda': kda
        }

    return hero_information


