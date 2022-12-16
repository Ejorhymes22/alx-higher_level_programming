#!/bin/bash
#displays the size of the body ofo response
curl -sI "$1" | grep 'Content-Length' | cut -d ' ' -f 2
