#!/usr/bin/python3
import requests
import threading

# Link to spam
url = ""

# All request fields present on page, this will differ from one link to another, so adjust accordingly.
data = {
    'cc_number: 4007000000027',
    'cc_expmonth : 00',
    'cc_expyear : 00',
    'cc_cvv: 000',
}

def make_request():
    while True:
        response = requests.post(url, data=data).text
        print(response)

threads = []

for i in range(50):
    t = threading.Thread(target=make_request)
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()

