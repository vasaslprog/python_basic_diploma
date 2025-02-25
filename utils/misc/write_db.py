import datetime
import json
import os

import requests

from database.models import Games


def writing_to_db():
    url = "https://livescore6.p.rapidapi.com/matches/v2/list-by-date"

    querystring = {"Category":"soccer","Date": your_date,"Timezone":"-7"}

    headers = {
        "x-rapidapi-key": os.getenv('API_KEY'),
        "x-rapidapi-host": "livescore6.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)

    data_api = json.loads(response.text)

    path_json = os.path.abspath(
        "C:/Users/proni/PycharmProjects/python_basic_diploma/database/data.json"
    )

    with open(path_json, "w") as test_file:
        json.dump(data_api, test_file, indent=4)
    with open(path_json, "r") as file_r:
        json_data = json.load(file_r)
    for i_game in json_data:
        for i_bookmakers in i_game["bookmakers"]:
            for i_markets in i_bookmakers["markets"]:
                for i_outcomes in i_markets["outcomes"]:
                    Games.create(
                        game_id=i_game["id"],
                        time_req=datetime.datetime.now(),
                        home_team=i_game["home_team"],
                        away_team=i_game["away_team"],
                        title=i_bookmakers["title"],
                        name_team=i_outcomes["name"],
                        price=i_outcomes["price"],
                    )
