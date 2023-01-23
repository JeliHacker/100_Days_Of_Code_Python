import os
import requests
from datetime import datetime, timedelta, date

class FlightSearch():
    #This class is responsible for talking to the Flight Search API.
    # Tequila by Kiwi

    sheet_rows = None

    # Get the current date and time
    now = datetime.now()

    today_plus_three_days = now + timedelta(days=3)
    today_plus_three_days = today_plus_three_days.strftime("%d/%m/%Y")

    # Add 6 months to the current date and time
    future_date = now + timedelta(days=180)

    today = now.strftime("%d/%m/%Y")
    today_plus_six_months = future_date.strftime("%d/%m/%Y")

    headers = {
        "Content-Type": "application/json",
        "apikey": os.environ.get("TEQUILA_API_KEY"),
        "Content-Encoding": "gzip",
        "dateFrom": today,
        "dateTo": today_plus_six_months
    }

    params = {
        # "apikey": os.environ.get("TEQUILA_API_KEY"),
        "fly_from": "LON",
        "date_from": today,
        "date_to": today_plus_three_days,
        "curr": "USD",
        "price_from": 0,
        "price_to": 30
    }

    url = "https://api.tequila.kiwi.com/v2/search"

    response = requests.get(url=url, headers=headers, params=params)

    # print(response.text)

    def set_sheet_rows(self, new_sheet_rows):
        self.sheet_rows = new_sheet_rows
        print(self.sheet_rows)
