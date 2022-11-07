import os
import requests
import app


# IMP INFO: Quota information: 30 requests every 1 minute
class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_iata_code(self, city_name):
        headers = {"apikey": os.environ['TEQUILA_API_KEY']}
        query = {"term": city_name, "location_types": "city"}
        iataCode = requests.get(url=f"{os.environ['TEQUILA_URL']}/locations/query", headers=headers, params=query)
        app.logger.info("Tequila API get call done!")
        return iataCode.json()["locations"][0]["code"]
