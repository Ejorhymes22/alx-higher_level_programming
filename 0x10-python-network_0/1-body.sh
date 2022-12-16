#!/bin/bash
#displays only body of response
curl -sI ubuntu@54.210.85.166 -O i; if grep -q "200 OK" i; then curl ubuntu@54.210.85.166; fi
