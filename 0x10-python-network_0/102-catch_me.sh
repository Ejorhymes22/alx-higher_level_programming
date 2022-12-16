#!/bin/bash
# this prints you got me!
curl -w 'You got me!' 0.0.0.0:5000/catch_me -s -o /dev/null;
