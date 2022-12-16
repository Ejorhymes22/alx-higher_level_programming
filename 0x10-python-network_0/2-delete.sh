#!/bin/bash
#displays only body of response
curl "$1" ; curl -X DELETE "$1"
