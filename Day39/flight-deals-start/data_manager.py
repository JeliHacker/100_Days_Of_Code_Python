import requests
import os



class DataManager:
    #This class is responsible for talking to the Google Sheet.
    url = "https://api.sheety.co/9136a8d3a5be37375170b62baa74d35e/day39FlightDeals/prices"

    headers = {
        "Authorization": os.environ.get("SHEETY_AUTH")
    }

    get_response = requests.get(url=url, headers=headers)
    prices = get_response.json()["prices"]

    def get_rows(self):
        get_response = requests.get(url=self.url, headers=self.headers)
        prices = get_response.json()["prices"]
        return prices
