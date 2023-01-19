# import config
import requests
import datetime
import json
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

params = {
    'query': input("Enter query here: "),
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 167,
    "age": 21
}

# query = {
#     "query": input("Enter query here: ")
# }

print(APP_ID)
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=endpoint, json=params, headers=headers)

exercise_info = json.loads(response.text)

print(type(exercise_info))
print("exercise info = ", exercise_info)
exercise_info_specific = exercise_info["exercises"][0]
duration = exercise_info["exercises"][0]['duration_min']
calories = exercise_info_specific["nf_calories"]
exercise = exercise_info_specific["user_input"]

today = datetime.date.today().strftime("%Y-%m-%d")
time = datetime.datetime.now().strftime("%H:%M:%S")

url = 'https://api.sheety.co/9136a8d3a5be37375170b62baa74d35e/100DaysOfCodeDay38MyWorkouts/workouts'
# url = 'https://api.sheety.co/jeligooch/100DaysOfCodeDay38MyWorkouts/workouts'

json = {
    "workout": {
        "date": today,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
    }
}

print(json)

sheety_headers = headers
sheety_headers["Authorization"] = os.environ.get("AUTH_TOKEN")

response = requests.post(url=url, json=json, headers=sheety_headers)

print(response.text)
print(response.status_code)