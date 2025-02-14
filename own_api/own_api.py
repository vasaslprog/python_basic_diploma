# import requests
# import json
# from dotenv import load_dotenv
# import os
# load_dotenv()
#
#
# def find_matches_by_date(your_date):
# 	url = os.getenv('URL_BY_DATE')
# 	querystring = {"Category":"soccer","Date": your_date,"Timezone":"-7"}
#
# 	headers = {
# 		"x-rapidapi-key": os.getenv('API_KEY'),
# 		"x-rapidapi-host": os.getenv('API_HOST')
# 	}
#
# 	response = requests.get(url, headers=headers, params=querystring)
# 	file_json = json.loads(response.text)
# 	with open("matches_by_date.json", "w", encoding="utf-8") as file:
# 		json.dump(file_json, file, indent=4)
