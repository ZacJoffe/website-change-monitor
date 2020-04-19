#!/usr/bin/env python3

import argparse
import requests
from bs4 import BeautifulSoup
import time
import smtplib, ssl

def get_source(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, "lxml")

parser = argparse.ArgumentParser(description='List the content of a folder')

parser.add_argument('-e', "--sender", help='Gmail sender address', required=True)
parser.add_argument('-p', "--password", help='Gmail sender password', required=True)
parser.add_argument('-r', "--receiver", help='Gmail reciever', required=True)
parser.add_argument('--url', help='URL to poll', required=True)
parser.add_argument('--sleep', type=int, help='Seconds to sleep before polling again, defaults to 60 seconds', default=60)

args = parser.parse_args()

gmail = args.sender
password = args.password
receiver_gmail = args.receiver
url = args.url
sleep = args.sleep

ssl_port = 465
ssl_context = ssl.create_default_context()
email_message = """\
Subject: Website has changed

{website} has changed!""".format(website=url)

print("Starting website polling...")

# get the initial source of the webpage, and sleep before trying again in the loop
source = get_source(url)
time.sleep(sleep)

while True:
    new_source = get_source(url)
    if source != new_source:
        # Create a secure SSL context
        with smtplib.SMTP_SSL("smtp.gmail.com", ssl_port, context=ssl_context) as server:
            server.login(gmail + "@gmail.com", password)
            server.sendmail(gmail, receiver_gmail + "@gmail.com", email_message)
        print("Change detected - email sent!")
        source = new_source

    time.sleep(sleep)

