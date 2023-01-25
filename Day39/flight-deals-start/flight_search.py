import os
import requests
from datetime import datetime, timedelta, date
from notification_manager import NotificationManager

class FlightSearch():
    #This class is responsible for talking to the Flight Search API.
    # Tequila by Kiwi

    notification = NotificationManager()

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
        "fly_to": "PAR",
        "date_from": today,
        "date_to": today_plus_three_days,
        "curr": "USD",
        "price_from": 0,
        "price_to": 330,
    }

    url = "https://api.tequila.kiwi.com/v2/search"

    response = requests.get(url=url, headers=headers, params=params)

    # print(response.text)

    def set_sheet_rows(self, new_sheet_rows):
        self.sheet_rows = new_sheet_rows
        # print(self.sheet_rows)

    def search_for_flights(self, city, price):
        self.params["fly_to"] = city
        self.params["price_to"] = price
        response = requests.get(url=self.url, headers=self.headers, params=self.params)
        # print(f"status = {response.status_code}")
        if len(response.json()["data"]) > 0:
            flight = response.json()["data"][0]
            print(flight)
            new_price = flight['price']
            print(f"price = {flight['price']}")
            cityFrom = flight['cityFrom'] + "-" + flight['flyFrom']
            print(f"from = {flight['cityFrom']}, {flight['flyFrom']}")
            cityTo = flight['cityTo'] + "-" + flight['flyTo']
            print(f"to = {flight['cityTo']}, {flight['flyTo']}")
            date1 = flight['local_departure']
            print(f"departure = {flight['local_departure']}")
            self.notification.alert_deal(new_price, cityFrom, cityTo, date1)

    def search_first_city(self):
        if len(self.sheet_rows) > 0:
            # print(self.sheet_rows[0]['iataCode'])
            self.search_for_flights(city=self.sheet_rows[0]['iataCode'])

    def search_all_cities(self):
        for row in self.sheet_rows:
            print("row = " + str(row))
            row_city = row['iataCode']
            # print(f"city = {row_city}")
            row_price = row['lowestPrice']
            # print(f"price = {row_price}")
            self.search_for_flights(row_city, row_price)
