#!/usr/bin/python3
# script sends request to URL and displays value of variable X-Request-Id
import requests
import sys

# check if url is provided as an argument
if len(sys.argv) != 2:
    print("Usage: {} <url>".format(sys.argv[0]))
    sys.exit(1)
# get the url
url = sys.argv[1]
# open the url and read the response
try:
    with requests.get(url) as response:
        if "X-Request-Id" in response.headers:
            print(response.headers["X-Request-Id"])
        else:
            print("None")
except requests.exceptions.HTTPError as error:
    print("Error code: {}".format(error))
