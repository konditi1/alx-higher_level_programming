#!/usr/bin/python3
# script that sends a request to url and displays response body
import sys
import requests
# check if url is provided as an argument
if len(sys.argv) != 2:
    print("Usage: {} <url>".format(sys.argv[0]))
    sys.exit()
# get the url
url = sys.argv[1]
# open the url and read the response
try:
    with requests.get(url) as response:
        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))
        else:
            print(response.text)
except requests.exceptions.HTTPError as error:
    print("Error code: {}".format(error.code))
