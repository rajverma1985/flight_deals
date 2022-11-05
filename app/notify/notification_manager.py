import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()


class NotificationManager:
    def __init__(self):
        pass

    @property
    def something(self):
        pass

    # This class is responsible for sending notifications with the deal flight details.
    pass


def tw_call():
    account_sid = os.environ['TW_ACCOUNT_SID']
    auth_token = os.environ['TW_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=f"whatsapp:{os.environ['TW_WATSAPP']}",
        body='Hello! This is an editable text message. You are free to change it and write whatever you like.',
        to=f"whatsapp:{os.environ['MY_NUMBER']}"
    )
    return message.sid
