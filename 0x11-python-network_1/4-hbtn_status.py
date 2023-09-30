#!/usr/bin/python3
#  script that fetches https://alx-intranet.hbtn.io/status
from urllib import request, error
# store the url in a variable
url = "https://alx-intranet.hbtn.io/status"
# open the url and read the response
try:
    with request.urlopen(url) as response:
        html1 = response.read()
        html = html1.decode("utf-8")
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
except error.HTTPError as error:
    print("Error code: {}".format(error.code))
