## TODO FIX THE CODE FROM RUNNING IF IT HITS A QUOTA LIMIT ON THE GET REQUEST.
import os
import requests
import logging.config
import logging

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('applogger')

sheety_url = f"{os.environ['SHEETY_ENDPOINT']}/flightDeals/prices"


# This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_sheets_data(self):
        response = requests.get(sheety_url)
        logger.info("Sheety API GET call done!")
        if 'errors' in response.json():
            logger.info(f"Sheety API GET call done! but we hit an error:\n {response.json()}")
        else:
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
            logger.info("Sheety API PUT call done!, the response is: %s".format(response.json()))
