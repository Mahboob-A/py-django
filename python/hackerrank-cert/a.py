# 250125, Saturday, 12.00 pm 

import requests

def exam(team: str, year: int) -> int:
    page = 1 

    data = []
    goals = 0

    home_url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={page}"

    total_pages = requests.get(home_url).json().get("total_pages")
    
#     while True: 
        
#         page = 1
        
#         home_url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={page}"
#         data = requests.get(home_url).json()
#         total_pages = data.get("total_pages")
#         for datablock in data:
#             goals += int(datablock["team1goals"])
        
    for i in range(1, total_pages+1):
        home_url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={i}"
        data = requests.get(home_url).json().get("data")

        for datablock in data:
            goals += int(datablock["team1goals"])

    page = 1
    for i in range(1, total_pages + 1):
        away_url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page={i}"
        data = requests.get(away_url).json().get("data")

        for datablock in data:
            goals += int(datablock["team2goals"])

    print(goals)


exam("Barcelona", 2011)
