# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

from sandbox import response
from pprint import pprint


sheet_data = [data for data in response.json()["prices"]]
# [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2},
# {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3},
# {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4},
# {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5},
# {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6},
# {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7},
# {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8},
# {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9},
# {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]


for data in sheet_data:
    if not data['iataCode']:
        print("its null")


