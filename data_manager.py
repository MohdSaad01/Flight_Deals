import requests
from flight_search import FlightSearch
from flight_data import FlightData
import os
from dotenv import load_dotenv

load_dotenv()
# Paste your Shetty username & password in .env file
username=os.getenv("SHETTY_USERNAME")
password=os.getenv("SHETTY_PASSWORD")

class DataManager:
    def __init__(self):
        self.auth=(username,password)
        self.flight_search=FlightSearch()
        self.flight_data=FlightData()
        self.update_iataCode()

    def update_iataCode(self):
        for row in self.flight_data.data:
            city=row["city"]
            id=row["id"]

            header={
                "Content-Type":"application/json"
            }

            body={
                "price":{
                    "iataCode":self.flight_search.get_iatacode(city)
                }
            }

            response=requests.put(url=f"https://api.sheety.co/09775ac5e90491fc43d9464fdf81328c/flightDeals/prices/{id}",headers=header,json=body,auth=self.auth)
