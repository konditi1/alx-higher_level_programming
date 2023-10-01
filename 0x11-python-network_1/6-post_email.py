#!/usr/bin/python3
# script that takes in a URL and an email
# sends a POST request to the passed URL with the email
# as a parameter, and displays the body of the response (decoded in utf-8)
import sys
import requests

# check if url and email is provided as an argument
if len(sys.argv) != 3:
    print("Usage: {} <url> <email>".format(sys.argv[0]))
    sys.exit(1)
# get the url and email
url = sys.argv[1]
email = sys.argv[2]
data = {'email': email}
# send a POST request to the passed URL with the email as a parameter
try:
    with requests.post(url, data=data) as response:
        html = response.text.encode('utf-8')
        print(html.decode('utf-8'))
except requests.exceptions.HTTPError as error:
    print("Error code: {}".format(error))
