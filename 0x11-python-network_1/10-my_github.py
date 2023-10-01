#!/ussr/bin/python3
""" Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: {} <username> <password>".format(argv[0]))
        exit(1)
    url = "https://api.github.com/user"
    data = {'username': argv[1], 'password': argv[2]}
    r = requests.post(url, data=data)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
