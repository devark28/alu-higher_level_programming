#!/bin/bash
# This script sends a request to a URL passed as an argument, and displays only the body of the response.
curl -sI "$1"