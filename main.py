import os
from dotenv import load_dotenv
import requests
from datetime import datetime

endpoint = "https://app.100daysofpython.dev"
exercise_input = input("Tell me which exercise you did: ")
sheet_endpoint = 'https://api.sheety.co/6fee232c9a12d653b244a91195e6ad98/workout/workouts'
load_dotenv()

headers = {
    "x-app-id": os.getenv("APP_ID"),
    "x-app-key": os.getenv("APP_KEY"),
}

params = {
    "query": exercise_input,
}

sheet_header = {
    "Authorization": os.getenv("AUTHORIZATION"),
}

today = datetime.now()
year = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

exercise_endpoint = f"{endpoint}/v1/nutrition/natural/exercise"
request = requests.post(url=exercise_endpoint, json=params, headers=headers)
health_endpoint = f"{endpoint}/healthz"
request1 = requests.get(url=health_endpoint)

data = request.json()["exercises"][0]
print(data)
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
print(type(os.getenv("SHEET_USER")))
print(os.getenv("SHEET_PASS"))
print(os.getenv("AUTHORIZATION"))
requests.get(url=sheet_endpoint)
responses = requests.post(url=sheet_endpoint, json=parameters, headers=sheet_header, auth=(os.getenv("SHEET_USER"), os.getenv("SHEET_PASS")))
responses.raise_for_status()
# body = {
#     "workout": {
#         "Date":
#     }
# }