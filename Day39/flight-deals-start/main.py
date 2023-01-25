#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

dataManager = DataManager()

sheet_rows = dataManager.get_rows()

flightSearch = FlightSearch()

notification = NotificationManager()


flightSearch.set_sheet_rows(sheet_rows)

flightSearch.search_all_cities()
