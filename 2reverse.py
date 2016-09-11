#!/usr/bin/python

# Step II: Reverse a string

import urllib
import sys


token = sys.argv[1]

## 
urlGetWord = "http://challenge.code2040.org/api/reverse"
data = urllib.urlencode({"token": token})
conn = urllib.urlopen(urlGetWord, data)
getWord = conn.read()
print type(getWord)
print getWord

## 
urlValidateW = "http://challenge.code2040.org/api/reverse/validate"
reverse = getWord[::-1]
print reverse
data2 = urllib.urlencode({"token": token, "string": reverse})
conn2 = urllib.urlopen(urlValidateW, data2)
response = conn2.read()
print response