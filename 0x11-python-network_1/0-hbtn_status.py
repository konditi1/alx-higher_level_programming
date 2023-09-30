#!/usr/bin/python3
#  script that fetches https://alx-intranet.hbtn.io/status
from urllib import request, error
# store the url in a variable
url = "https://alx-intranet.hbtn.io/status"
# open the url and read the response
try:
    with request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))
except error.HTTPError as error:
    print("Error code: {}".format(error.code))
