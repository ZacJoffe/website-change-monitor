#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import time
import smtplib, ssl

def get_source(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, "lxml")

port = 465  # For SSL
email = input("Email: ")
password = input("Password: ")
url = input("URL: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(email, password)

source = get_source(url)

while True:
    new_source = get_source(url)
    if source == new_source:
        server.sendmail(email, "zacharyjoffe@gmail.com", "Change in website: " + url)
    time.sleep(60)

