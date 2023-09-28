#!/bin/bash
# post request to url and display body of response
curl -s POST -d email=test@gmail.com -d subject="I will always be here for PLD" "$1"
