# 250125, Saturday, 12.00 pm

import requests


def exam(year: int) -> int:

    total_draws = 0 
    for goal in range(0, 11):
        ulr = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1goals={goal}&team2goals={goal}&page=1"
        total = requests.get(ulr).json().get("total")
        total_draws += total
    
    return total_draws  


exam(2011)
