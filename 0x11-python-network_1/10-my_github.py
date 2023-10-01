#!/usr/bin/python3
""" Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # git hub api
    url = "https://api.github.com/user"
    username = argv[1]
    password = argv[2]
    data = HTTPBasicAuth(username, password)
    response = requests.post(url, auth=data)
    print(response.json().get("id"))
