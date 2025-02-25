import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()


def find_matches_by_date(your_date):
	url = "https://livescore6.p.rapidapi.com/matches/v2/list-by-date"
	querystring = {"Category":"soccer","Date": your_date,"Timezone":"-7"}

	headers = {
		"x-rapidapi-key": os.getenv('API_KEY'),
		"x-rapidapi-host": "livescore6.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)
	file_json = json.loads(response.text)
	with open("matches_by_date.json", "w", encoding="utf-8") as file:
		json.dump(file_json, file, indent=4)
