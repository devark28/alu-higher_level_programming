#!/bin/bash
# This script shows all http methods the server will accept.
curl -sI "$1" | awk '/Allow/ {print $2, $3, $4}'
