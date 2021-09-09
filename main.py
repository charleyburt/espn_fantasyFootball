import requests

league_id = 1535095
year = 2020

url = "https://fantasy.espn.com/apis/v3/games/ffl/leagueHistory/" + \
      str(league_id) + "?seasonId=" + str(year)
      
print('hi')

r = requests.get(url, params={"view": "mMatchup"})
d = r.json()[0]


print('hi')