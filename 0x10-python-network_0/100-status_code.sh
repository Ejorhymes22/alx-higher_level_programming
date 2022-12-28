#!/bin/bash
# displays the status code using curl
curl -s -o /dev/null -w "% {http_code}" "$1"
