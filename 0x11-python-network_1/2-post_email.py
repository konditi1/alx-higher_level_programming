#!/usr/bin/python3
# script that takes in a URL and an email
# sends a POST request to the passed URL with the email
# as a parameter, and displays the body of the response (decoded in utf-8)
import sys
from urllib import request, error, parse

# check if url and email is provided as an argument
if len(sys.argv) != 3:
    print("Usage: {} <url> <email>".format(sys.argv[0]))
    sys.exit()
# get the url and email
url = sys.argv[1]
email = sys.argv[2]
data = {'email': email}
data = parse.urlencode(data).encode('utf-8')
req = request.Request(url, data=data, method='POST')
try:
    with request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        print(html)
except error.HTTPError as error:
    print("Error code: {}".format(error.code))
