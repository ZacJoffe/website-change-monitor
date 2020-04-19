#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import time
import smtplib, ssl

def get_source(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, "lxml")

gmail = input("Gmail sender: ")
password = input("Password: ")
receiver_gmail = input("Gmail receiver: ")
url = input("URL: ")

port = 465  # For SSL
context = ssl.create_default_context()
message = """\
Subject: Website has changed

{website} has changed!""".format(website=url)

print("Starting website polling...")

source = get_source(url)
time.sleep(60)

while True:
    new_source = get_source(url)
    if source != new_source:
        # Create a secure SSL context
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(gmail + "@gmail.com", password)
            server.sendmail(gmail, receiver_gmail + "@gmail.com", message)
        print("Change detected - email sent!")

    time.sleep(60)

