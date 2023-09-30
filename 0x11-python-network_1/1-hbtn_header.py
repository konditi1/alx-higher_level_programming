#!/usr/bin/python3
# script sends request to URL and displays value of variable X-Request-Id
from urllib import request, error
import sys
# check if url is provided as an argument
if len(sys.argv) != 2:
    print("Usage: {} <url>".format(sys.argv[0]))
    sys.exit()
# get the url
url = sys.argv[1]
# open the url and read the response
try:
    with request.urlopen(url) as response:
        # check if X-Request-Id is in the header
        if "X-Request-Id" in response.headers:
            print(response.headers["X-Request-Id"])
        else:
            print("None")
except error.HTTPError as error:
    print("Error code: {}".format(error.code))
