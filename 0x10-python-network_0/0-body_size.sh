#!/bin/bash
# file to send request to URL and display size in bytes
  curl -s $1 | wc -c
