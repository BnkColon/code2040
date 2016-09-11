#!/usr/bin/python

#Step III: Needle in a haystack

import urllib
import ast
import sys


token = sys.argv[1]

# Get the dictionary
urlGetDictionary = 'http://challenge.code2040.org/api/haystack'
data = urllib.urlencode({"token": token})
conn = urllib.urlopen(urlGetDictionary, data)
getDictionary = conn.read()
dictionary = ast.literal_eval(getDictionary)

# Validate
urlValidation= 'http://challenge.code2040.org/api/haystack/validate'
word = dictionary["needle"]
getIndex=dictionary['haystack'].index(word)
data2 = urllib.urlencode({"token": token, "needle": getIndex})
conn2 = urllib.urlopen(urlValidation, data2)
response = conn2.read()
print response