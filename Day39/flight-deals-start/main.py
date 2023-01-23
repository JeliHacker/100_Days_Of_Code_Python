#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

dataManager = DataManager()

sheet_rows = dataManager.get_rows()

# print(sheet_rows)

flightSearch = FlightSearch()

flightSearch.set_sheet_rows(sheet_rows)
