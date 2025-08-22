# main.py
# Entry point of the Flight Deals project
# This script initializes the data manager and flight search processes.
# When run, it will update IATA codes, check for cheaper flights, and send notifications if needed.

# Import necessary classes
from flight_search import FlightSearch
from data_manager import DataManager

# Initialize the DataManager
# This will fetch flight data from the Google Sheet and update IATA codes if necessary
dataManager = DataManager()

# Initialize the FlightSearch
# This will search for flights based on the data from DataManager
# If a cheaper flight is found, notifications will be sent to users
flightSearch = FlightSearch()

# Program execution complete
# All actions are automatically triggered by class initialization
