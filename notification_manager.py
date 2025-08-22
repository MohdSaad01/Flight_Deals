import os
from dotenv import load_dotenv
from twilio.rest import Client
import requests
import smtplib

load_dotenv()
# Paste your Shetty username & password in .env file
username=os.getenv("SHETTY_USERNAME")
password=os.getenv("SHETTY_PASSWORD")

# Paste your Twilio API credentials in .env file
account_sid=os.getenv("TWILIO_AUTH_ID")
account_token=os.getenv("TWILIO_AUTH_TOKEN")

# Paste your Gmail address & app password in .env file
mail = os.getenv("SMTP_MAIL")
mail_password= os.getenv("SMTP_PASS")

class NotificationManager:
    def __init__(self,cheapest_price,city,cheap_date):
        self.auth=(username,password)
        self.client=Client(account_sid,account_token)
        self.get_customer_email(cheapest_price,city,cheap_date)

    def get_customer_email(self,cheapest_price,city,cheap_date):

        header = {
            "Content-Type": "application/json"
        }

        get_email=requests.get(url="https://api.sheety.co/b85efa7910aa00c100eb8e01bdbc34dc/flightDeals/users",headers=header,auth=self.auth)
        email_data=get_email.json()["users"]
        email_list = [row["email"] for row in email_data]
        self.send_mails(cheapest_price,city,cheap_date,email_list)

    def send_mails(self,cheapest_price,city,cheap_date,email_list):
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user=mail,password=mail_password)
            for emails in email_list:
                connection.sendmail(
                        from_addr=mail,
                        to_addrs=emails,
                        msg=f"Subject:Low Price Alert!\n\n Low Price alert! Only GBP{cheapest_price} to fly from London to {city}, on {cheap_date}"
                     )
