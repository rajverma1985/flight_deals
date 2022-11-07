# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

from app.data.data_manager import DataManager
from app.search.flight_search import FlightSearch
from pprint import pprint

search = FlightSearch()
data = DataManager()

sheet_data = data.get_sheets_data()


def run_app():
    for row in sheet_data:
        if not row['iataCode']:
            row['iataCode'] = search.get_iata_code(row['city'])
            data.destination_data = sheet_data
            data.update_iatacode()
