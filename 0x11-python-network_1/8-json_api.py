#!/usr/bin/python3
# script that takes a letter and sends a post request to url
# with the letter as a parameter
import sys
import requests

if __name__ == "__main__":
    # check if letter is provided as an argument
    if len(sys.argv) != 1:
        letter = ""
    else:
        letter = sys.argv[1]
    data = {'q': letter}
    # send a POST request to the passed URL with the letter as a parameter
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        # If the response body is properly JSON formatted
        json_dict = response.json()
        if json_dict == {}:
            print("No result")
        else:
            print(f"[{json_dict['id']}] {json_dict['name']}")
    except ValueError:
        print("Not a valid JSON")
