'''
Extracting Data from JSON:

The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the 
JSON data, compute the sum of the numbers in the file and enter the sum below:

Data: http://py4e-data.dr-chuck.net/comments_1377123.json

Data Format
The data consists of a number of names and comment counts in JSON as follows:

{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}
'''

import json
import ssl
import urllib.request, urllib.parse, urllib.error


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

lst = list()
link = input('Enter location:')
# Use urllib to read the url
data = urllib.request.urlopen(link).read()
# load JASON data
info = json.loads(data)

# extract the comment counts from the JSON data
print('Count:', len(info['comments']))

for item in info['comments']:
    lst.append(item['count'])
print('Sum:', sum(lst))
