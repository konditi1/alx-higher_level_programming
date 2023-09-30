#!/usr/bin/python3
#  script that fetches https://alx-intranet.hbtn.io/status
from urllib import request
# store the url in a variable
url = "https://alx-intranet.hbtn.io/status"
# open the url and read the response

with request.urlopen(url) as response:
    html1 = response.read()
    html = html1.decode("utf-8")
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
