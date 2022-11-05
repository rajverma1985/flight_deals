# Download the helper library from https://www.twilio.com/docs/python/install
import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# Find your Account SID and Auth Token in Account Info and set the environment variables.
# See http://twil.io/secure


response = requests.get(f"{os.environ['SHEETY_ENDPOIN']}/flightDeals/prices")
