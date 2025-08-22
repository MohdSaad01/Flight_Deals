import requests
import os
from dotenv import load_dotenv

load_dotenv()
# Paste your Shetty username & password in .env file
username=os.getenv("SHETTY_USERNAME")
password=os.getenv("SHETTY_PASSWORD")

class FlightData:
    def __init__(self):
        self.auth=(username,password)
        self.response=requests.get(url="https://api.sheety.co/b85efa7910aa00c100eb8e01bdbc34dc/flightDeals/prices",auth=self.auth)
        self.data=self.response.json()["prices"]
        for i in range(0,4):
            self.city=self.data[i]["city"]