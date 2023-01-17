import config
import requests
import datetime
import json

APP_ID = config.APP_ID
API_KEY = config.API_KEY

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

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=endpoint, json=params, headers=headers)
exercise_info = json.loads(response.text)
print(type(exercise_info))
exercise_info_specific = exercise_info["exercises"][0]
duration = exercise_info["exercises"][0]['duration_min']
calories = exercise_info_specific["nf_calories"]
exercise = exercise_info_specific["user_input"]

today = datetime.date.today().strftime()
time = datetime.datetime.now().strftime("%H:%M:%S")

url = 'https://api.sheety.co/9136a8d3a5be37375170b62baa74d35e/100DaysOfCodeDay38MyWorkouts/workouts'

json = {
    "Date": today,
    "Time": time,
    "Exercise": exercise,
    "Duration": duration,
    "Calories": calories,
}

print(json)

# response = requests.post(url=url, json=json, params=json)
# print(response.text)