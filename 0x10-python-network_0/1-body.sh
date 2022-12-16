#!/bin/bash
#displays only body of response
curl -sIL "$1" -O i.txt; if grep -q "200 OK" i.txt; then curl -L "$1"; fi
