#!/bin/bash
# send a post request with variables
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
