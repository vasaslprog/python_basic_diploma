import requests

url = "https://livescore6.p.rapidapi.com/matches/v2/list-by-date"

querystring = {"Category":"soccer","Date":"20201028","Timezone":"-7"}

headers = {
	"x-rapidapi-key": "ec925d340cmsh274017ddced15cep1715cbjsnb3f1eb6cac5f",
	"x-rapidapi-host": "livescore6.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())