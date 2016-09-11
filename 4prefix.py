#!/usr/bin/python

# Step IV: Prefix

import urllib
import ast
import sys


token = sys.argv[1]

# Get the dictionary
urlGetDictionary = 'http://challenge.code2040.org/api/prefix'
data = urllib.urlencode({"token": token})
conn = urllib.urlopen(urlGetDictionary, data)
getDictionary = conn.read()
print 'get' + getDictionary
dictionary = ast.literal_eval(getDictionary)

# Create new array 
prefix = dictionary['prefix']
print prefix
array = dictionary['array']
print array
newArray = [] 
for k in array:
	if prefix  == k[0:len(prefix)]:
		continue
	else:
		newArray.append(k)
print newArray	

# Send
urlValidation= 'http://challenge.code2040.org/api/prefix/validate'
d = {"token": token, "array": newArray}
print d
data2 = urllib.urlencode(d)
print data2
conn2 = urllib.urlopen(urlValidation, data2)
response = conn2.read()
print response

