import requests
from twilio.rest import Client
import config

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = config.OWM_API_KEY
account_sid = "AC0c1f13db0652fb5602c45ca64772c17d"
auth_token = config.AUTH_TOKEN

# lat = 34.080292
# lon = -118.404678
lat = 31.886016
lon = -94.261884

weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_='+13149364762',
        to='+18593190444'
    )

    print(message)
    print(message.status)
