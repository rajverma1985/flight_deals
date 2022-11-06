import os
import requests
from dotenv import load_dotenv

load_dotenv()
sheety_url = f"{os.environ['SHEETY_ENDPOINT']}/flightDeals/prices"


# This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_sheets_data(self):
        response = requests.get(sheety_url)
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_iatacode(self):
        for city_dict in self.destination_data:
            data = {'price':
                {
                    'iataCode': city_dict['iataCode']
                }
            }
            response = requests.put(url=f"{sheety_url}/{city_dict['id']}", json=data)
            response.raise_for_status()
            print(response.text)
