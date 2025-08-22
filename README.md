# ✈️ Flight Deals Notifier ✈️

Automatically tracks flight prices from London to various destinations and sends email notifications to users when cheaper flights are found. This project integrates **Amadeus API** for flight data, **Sheety API** for Google Sheet management, and **SMTP** for email alerts.

---

## Features
- Fetches cities and current flight prices from a Google Sheet.
- Updates IATA codes automatically if missing.
- Searches flights using the Amadeus API.
- Sends email notifications to users when a flight price drops below the recorded value.
- Can be extended to send SMS notifications via Twilio.

---

### 2. Accounts and APIs

#### Amadeus API
- Sign up at [Amadeus for Developers](https://developers.amadeus.com/).  
- Get your `API_KEY` and `API_SECRET`.  

#### Sheety API
- Create a Google Sheet to store flight prices with the following columns:  
  `id`, `city`, `iataCode`, `lowestPrice`  
- Use [Sheety](https://sheety.co/) to turn your Google Sheet into an API.  
- Get `USERNAME` and `PASSWORD` for basic authentication.  

#### Google Form for Clients
- Create a Google Form to collect user emails.  
- Responses should be stored in a Google Sheet.  
- Use Sheety to turn this Sheet into an API for fetching user emails.  

---

### 3. Environment Variables
Create a `.env` file in the root folder with the following keys:

```text
SHETTY_USERNAME=your_sheety_username
SHETTY_PASSWORD=your_sheety_password
AMADEUS_API_KEY=your_amadeus_api_key
AMADEUS_API_SECRET=your_amadeus_api_secret
SMTP_MAIL=your_email@gmail.com
SMTP_PASS=your_email_password
TWILIO_AUTH_ID=your_twilio_sid (optional)
TWILIO_AUTH_TOKEN=your_twilio_token (optional)


**Author's Note:**
This is one of those projects that took me several days to build. I was just focused on completing it,
so please excuse some small beginner mistakes in the code. The main goal was to get it fully working and automated. 🙏
