#!/bin/bash
#displays only body of response
curl -sI "$1" -O i.txt; if grep -q "200 OK" i.txt; then curl "$1"; fi
