import datetime
import os
import sys
from typing import List

from database.models import Games
import json


def sorted_info_by_league() -> List:
    list_of_APL_matches = []
    script_dir = os.path.dirname(sys.argv[0])
    with open(os.path.join(script_dir, "matches_by_date.json"), "r") as file:
        j_file = json.load(file)
    for i_champs in j_file["Stages"]:
        if i_champs["Sid"] == '18173':
            for i_info in i_champs["Events"]:

                if i_info["Eps"] == "NS":
                    final_score = "матч не завершен"
                else:
                    final_score = i_info["Tr1"] + " : " + i_info["Tr2"]
                time_begin = str(int(str(i_info["Esd"])[8:10]) + 10) + ":" + str(i_info["Esd"])[10:12]

                match_id = i_info["Eid"]  # id конкретного матча, нужен, чтобы найти матч в другом запросе API
                team1 = i_info["T1"][0]["Nm"]  # команда хозяев
                team2 = i_info["T2"][0]["Nm"]  # команда гостей
                team1_id = i_info["T1"][0]["ID"]  # id команды хозяев
                team2_id = i_info["T2"][0]["ID"]  # id команды гостей - для будущих изменений проекта
                list_of_APL_matches.append(f"{time_begin} {team1} - {team2}")

                Games.create(
                game_id=match_id,
                time_req=datetime.datetime.now(),
                home_team=team1,
                away_team=team2,
                score=final_score,
                )

    return list_of_APL_matches
