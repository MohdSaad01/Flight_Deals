import os
from dotenv import load_dotenv
import requests
from flight_data import FlightData
from datetime import datetime,timedelta
from notification_manager import NotificationManager

load_dotenv()
# Paste your Amadeus API credentials in .env file
Api_Key=os.getenv("AMADEUS_API_KEY")
Api_Secret=os.getenv("AMADEUS_API_SECRET")

class FlightSearch:
    def __init__(self):
        self.token=self.new_token()
        self.flight_data = FlightData()
        for row in self.flight_data.data:
            self.sheet_price=row["lowestPrice"]
            self.city = row["city"].upper()
            self.iata=self.get_iatacode(self.city)
            self.search_flight()

    def new_token(self):
        header={
            "Content-Type":"application/x-www-form-urlencoded"
        }

        body={
            "grant_type": "client_credentials",
            "client_id":Api_Key,
            "client_secret":Api_Secret
        }

        response=requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token",headers=header,data=body)
        return response.json()["access_token"]

    def get_iatacode(self,city):
        header={
            "Authorization":f"Bearer {self.token}"
        }

        parameter={
            "keyword":city,
            "subType":"CITY"
        }

        response=requests.get(url="https://test.api.amadeus.com/v1/reference-data/locations",headers=header,params=parameter)
        return response.json()["data"][0]["iataCode"]

    def search_flight(self,is_direct=True):

        header = {
            "Authorization": f"Bearer {self.token}"
        }

        cheapest_price= self.sheet_price
        cheap_date=None

        for i in range(1, 2): #Got it down only for checking
            departure_date = (datetime.today() + timedelta(days=i)).strftime("%Y-%m-%d")

            parameter={
                "originLocationCode":"LON",
                "destinationLocationCode":self.iata,
                "departureDate":departure_date,
                "adults":1,
                "currencyCode":"GBP",
                "nonStop":str(is_direct).lower()
            }
            response = requests.get(url="https://test.api.amadeus.com/v2/shopping/flight-offers",headers=header,params=parameter)
            flights=response.json().get("data",[])

            if not flights:
                continue

            price=float(flights[0]["price"]["total"])
            if price<cheapest_price:
                cheapest_price=price
                cheap_date=departure_date

            if not cheap_date and is_direct:return self.search_flight(is_direct=False)

            if cheap_date:
                NotificationManager(cheapest_price,self.city,cheap_date)
