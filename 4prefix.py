#!/usr/bin/python

# Step IV: Prefix

import requests # http://docs.python-requests.org/en/master/user/quickstart/
import json
import loggin
import ast
import sys

# http://docs.python-requests.org/en/master/api/
# Enabling debugging at http.client level (requests->urllib3->http.client)
# you will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# the only thing missing will be the response.body which is not logged.
try: # for Python 3
    from http.client import HTTPConnection
except ImportError:
    from httplib import HTTPConnection
HTTPConnection.debuglevel = 1

logging.basicConfig() # you need to initialize logging, otherwise you will not see anything from requests
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

token = sys.argv[1]

# Get the dictionary for the challenge
urlGetDictionary = 'http://challenge.code2040.org/api/prefix'
d = {'token':token} # payload
r = requests.post(urlGetDictionary, json = d) # request
dictionary = json.loads(r.text)
print type(dictionary)

# Create new array
prefix = dictionary['prefix']
print prefix
array = dictionary['array']
print array
newArray = [] 
for k in array:
	if k.startswith(prefix):
		continue
	else:
		newArray.append(k)
print newArray	

# Send the response to validate
urlValidation= 'http://challenge.code2040.org/api/prefix/validate'
d = {"token": token, "array": newArray}
print d
r = requests.post(urlValidation, json = d) # request
response = r.text
print response

