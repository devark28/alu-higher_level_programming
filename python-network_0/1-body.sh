#!/bin/bash
# This script sends a request to a URL passed as an argument, and displays only the body of 200 status code responses.
curl -s "$1" | awk '/200/ {print $0}'
