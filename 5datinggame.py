#!/usr/bin/python

# Step V: The dating game

import requests # http://docs.python-requests.org/en/master/user/quickstart/
import sys
import logging
import json
import dateutil.parser as dp

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

# Get the dictionary
urlGetDictionary = 'http://challenge.code2040.org/api/dating'
d = {'token':token} # dictionary of the token
r = requests.post(urlGetDictionary, json = d) # request
dictionary = json.loads(r.text)
print '-------------'
print type(dictionary) # <type 'dict'>
print dictionary # {u'datestamp': u'2016-10-21T09:56:33Z', u'interval': 125303}

# Get Take the keys
datestamp = dictionary['datestamp']
interval = dictionary['interval']
print datestamp, interval
print type(datestamp), type(interval)

# Change datestamp to seconds
parsedDatestamp = dp.parse(datestamp)
datestampInSeconds = parsedDatestamp.strftime('%s')
print datestampInSeconds

# Add the interval to the date
#sumBoth =

# Send the result
