#!/usr/bin/bash
curl -sI "$1" | grep "Content-Length"