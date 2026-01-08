import os
import requests
from datetime import datetime

endpoint = "https://app.100daysofpython.dev"
exercise_input = input("Tell me which exercise you did: ")
sheet_endpoint = 'https://api.sheety.co/6fee232c9a12d653b244a91195e6ad98/workout/workouts'


headers = {
    "x-app-id": os.environ["app_id"],
    "x-app-key": os.environ["app_key"],
}

params = {
    "query": exercise_input,
}

sheet_header = {
    "Authorization: Basic emVsdGk6NDkya2ZqYXVzaGdGSg==",
}

today = datetime.now()
year = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

exercise_endpoint = f"{endpoint}/v1/nutrition/natural/exercise"
request = requests.post(url=exercise_endpoint, json=params, headers=headers)
health_endpoint = f"{endpoint}/healthz"
request1 = requests.get(url=health_endpoint)

data = request.json()["exercises"][0]
exercise_name = data["name"]
print(data)
duration = data["duration_min"]
calories = data["nf_calories"]
print(f"{year} - {time} - {exercise_name} - {duration} - {calories}")

parameters = {
    "workout": {
        "date": year,
        "time": time,
        "exercise": exercise_name.title(),
        "duration": duration,
        "calories": calories,
    }
}

requests.get(url=sheet_endpoint)
responses = requests.post(url=sheet_endpoint, json=parameters, auth=(os.environ["username"], os.environ["password"]))
responses.raise_for_status()
# body = {
#     "workout": {
#         "Date":
#     }
# }