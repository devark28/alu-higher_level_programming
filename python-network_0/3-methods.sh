#!/bin/bash
# This script sends a request to a URL passed as an argument, and displays the body of the response.
curl -sX OPTIONS "$1" -i | awk '/Allow/ {print $2}'
