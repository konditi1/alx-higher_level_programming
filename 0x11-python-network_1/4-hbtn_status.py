#!/usr/bin/python3
#  script that fetches https://alx-intranet.hbtn.io/status
import requests
# store the url in a variable
url = "https://alx-intranet.hbtn.io/status"
# open the url and read the response

with requests.get(url) as response:
    html = response.text
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
