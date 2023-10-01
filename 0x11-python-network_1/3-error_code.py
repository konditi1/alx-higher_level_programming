#!/usr/bin/python3
# script that sends a request to url and displays response body
import sys
from urllib import request, error
# check if url is provided as an argument
if len(sys.argv) != 2:
    print("Usage: {} <url>".format(sys.argv[0]))
    sys.exit()
# get the url
url = sys.argv[1]
# open the url and read the response
try:
    with request.urlopen(url) as response:
        html = response.read().decode('utf-8')
        print(html)
except error.HTTPError as error:
    print("Error code: {}".format(error.code))
