#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import time
import smtplib, ssl

def get_source(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, "lxml")

port = 465  # For SSL
gmail = input("Gmail: ")
password = input("Password: ")
url = input("URL: ")

# Create a secure SSL context
context = ssl.create_default_context()
message = """\
Subject: Website has changed

{website} has changed!""".format(website=url)

source = get_source(url)

while True:
    new_source = get_source(url)
    if source == new_source:
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(gmail + "@gmail.com", password)
            server.sendmail(gmail, "zacharyjoffe@gmail.com", message)
        print("Change detected - email sent!")

    time.sleep(60)

