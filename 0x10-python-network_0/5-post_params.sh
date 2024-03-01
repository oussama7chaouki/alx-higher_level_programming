#!/bin/bash
# sends a POST request to a given URL with some variables.
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
