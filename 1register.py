#!/usr/bin/python

# Step I: Registration
#$ python 1register.py <token>

import urllib
import json
import string
import sys


token = sys.argv[1]
githubURL= "https://github.com/BnkColon/code2040"
# Create the dictionary with the token and github
data = urllib.urlencode({"token": token, "github": githubURL})

url = "http://challenge.code2040.org/api/register"

conn = urllib.urlopen(url, data)
print conn.read()
