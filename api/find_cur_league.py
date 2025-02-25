def sorted_info_by_league():
    import json
    list_of_APL_matches = []
    count_match = 0

    with open("../matches_by_date.json", "r") as file:
        j_file = json.load(file)
    for i_champs in j_file["Stages"]:
        if i_champs["Sid"] == '18173':
            for i_info in i_champs["Events"]:

                if i_info["Eps"] == "NS":
                    count_match += 1
                    time_begin = str(int(str(i_info["Esd"])[8:10]) + 10) + ":" + str(i_info["Esd"])[10:12]
                    nr_tour = i_info["ErnInf"]  # номер тура чемпионата
                    match_id = i_info["Eid"]  # id конкретного матча, нужен, чтобы найти матч в другом запросе API
                    team1 = i_info["T1"][0]["Nm"]  # команда хозяев
                    team2 = i_info["T2"][0]["Nm"]  # команда гостей
                    team1_id = i_info["T1"][0]["ID"]  # id команды хозяев
                    team2_id = i_info["T2"][0]["ID"]  # id команды гостей
                    list_of_APL_matches.append(f"Номер тура: {nr_tour},{time_begin} Команда хозяев {team1} : {team2} Команда гостей")
                    # print(f"Время начала: {time_begin} Команда хозяев {team1} : {team2} Команда гостей")
    # print(list_of_APL_matches)
    return list_of_APL_matches
