'''
Calling a JSON API:

The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that 
data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a 
place as within Google Maps.

API End Points:

To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:
http://py4e-data.dr-chuck.net/json?

This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as 
often as you like. If you visit the URL with no parameters, you get "No address..." response.
To call the API, you need to include a key= parameter and provide the address that you are requesting as the 
address= parameter that is properly URL encoded using the urllib.parse.urlencode() function as shown in 
http://www.py4e.com/code3/geojson.py

Test Data / Sample Execution:

Enter location: South Federal University
Retrieving http://...
Retrieved 2146 characters
Place id ChIJLzabHQ7i2IgRzeZb_AgUj0Q
'''
import json
import ssl
import urllib.request, urllib.parse, urllib.error

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

while True:
    address = input('Enter location:')
    if len(address) < 1: break

    parms = {'address': address, 'key': api_key}
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving:', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
        print(js)

    # if not js or 'status' not in js or js['status'] != 'OK':
    #     print('====Failure To Retrieve ====')
    #     print(data)
    #     continue
    # print(json.dumps(js, indent = 4))

    print('place_id:', js['results'][0]['place_id'])
