'''
Extracting Data from XML:
The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from 
the XML data, compute the sum of the numbers in the file.

Data Format and Approach
The data consists of a number of names and comment counts in XML as follows:

<comment>
  <name>Matthias</name>
  <count>97</count>
</comment>

You are to look through all the <comment> tags and find the <count> values sum the numbers.

Data: http://py4e-data.dr-chuck.net/comments_1377122.xml

To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for 
any tag named 'count' with the following line of code:

counts = tree.findall('.//count')


Sample Execution:

Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
Retrieved 4189 characters
Count: 50
Sum: 2...
'''

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0
newlist = list()
link = input('Enter location:')
print('Retrieving:', link)
url = urllib.request.urlopen(link).read()

for i in url:
    count += 1
print('Retrieved ' + str(count) + ' characters')

tree = ET.fromstring(url)
lst = tree.findall('comments/comment')
print('Count:', len(lst))

for tag in lst:
    newlist.append(int(tag.find('count').text))
print('Sum:', sum(newlist))
