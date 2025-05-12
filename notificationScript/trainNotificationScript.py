# Imports
# Loading environment  variables from .env 
from dotenv import load_dotenv
# Accesses system environment variables
import os
# Time
import time
# HTTP Requests
import requests
# Parses HTML content
from bs4 import BeautifulSoup
# Adds desktop notification
from plyer import notification
# Sends SMS via Twilio account
from twilio.rest import Client
# Renders Javascript so we can access dynamic table
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# Setup Selenium (you need chromedriver installed or use webdriver-manager)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in background
options.add_argument("--log-level=3")  # Suppress most logs
driver = webdriver.Chrome(options=options)

# Loading environment variables from .env file
load_dotenv()

# Get the variables from the .env for messaging
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
messaging_service_sid = os.getenv("MESSAGING_SERVICE_SID")
my_number = os.getenv("MY_NUMBER")

# Function to send a text message using Twilio
def send_text_notification(line, station):
    # Twilio client with .env credentials
    client = Client(account_sid, auth_token)

    # Creates and sends message
    message = client.messages.create(
        body=f"Trains on the {line} line from {station} Stn may be delayed.\nCheck your transperth and consider using Bus services or driving.",
        messaging_service_sid=messaging_service_sid,
        to=my_number
    )
    
    # Print confirmation in terminal with message SID
    print("Twilio text sent! SID:", message.sid)

# User inputs which train line and station they'd like to receive information for
line = input("Please Enter Train line e.g. Yanchep    ")
station = input("Please Enter Train Station e.g. Perth    ")

# Adding headers to mimic a real browser (to avoid getting blocked)
HEADERS = {"User-Agent": "Mozilla/5.0"}

# Function to check if services are on time
def check_status(line, station):
    try:
        # Set the URL for the given train line and station
        URL = f"https://www.transperth.wa.gov.au/Timetables/Live-Train-Times?line={line}%20Line&station={station}%20Stn"
        # Send a GET request to the courses page
        driver.get(URL)
        # Allow time for JS to load if needed
        #time.sleep(5)
        html = driver.page_source
        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        # Extract all text only content from HTML
        table = soup.find('table', {'id': 'tblStationStatus'})
        
        if not table:
            print(f"{line} line status table not found... Track likely under maintenance, service delays or network error.")
            return False
        else:
            # Extract all rows from the tbody
            rows = table.find('tbody').find_all('tr')
            # Set Station info to unknown until checked
            departure = " - "
            destination = " - "
            description = " - "
            status = 'Unknown'
            # Only continue to check rows if status is On Time
            for row in rows:
                # "Last Updated" row has only 1 cell
                cols = row.find_all('td')
                if len(cols) == 4:
                    departure = cols[0].get_text(strip=True)
                    destination = cols[1].get_text(strip=True)
                    description = cols[2].get_text(strip=True)
                    status = cols[3].get_text(strip=True)
                    if status != "On Time":
                        break
                    # print table to terminal
                    print(f"{departure} | {destination} | {description} | {status}")
                elif len(cols) == 1:
                    # Handle the "Last Updated" row
                    last_updated = cols[0].get_text(strip=True)
                    print(f"...\n{last_updated}")
            
            if status != "On Time":
                # Send pc notification that services are delayed
                notification.notify(
                    title=f"Your train service to {destination} is delayed",
                    message=f"{line} line services may be delayed for {station} Stn.\n {departure} | {destination} | {description} | {status}",
                    timeout=15
                    )
                # Call the send text function to send a text message via Twilio
                send_text_notification(line, station)
                return False
            # Send pc notification that services are on time
            else:
                notification.notify(
                    title=f"{line} line train services on time!",
                    message=f"{line} line train services are on schedule for {station} Stn.",
                    timeout=13
                    )
                return True       
    # Handle errors    
    except Exception as e:
        print("Error during check:", e)
        return True

# Infinite loop to check every 5 minutes until train services restored
while True:
    if check_status(line, station):
        break
    time.sleep(300)
