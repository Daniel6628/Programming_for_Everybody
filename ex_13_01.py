'''
Scraping Numbers from HTML using BeautifulSoup:

The program will use urllib to read the HTML from the data files below, and parse the data, 
extracting numbers and compute the sum of the numbers in the file.
File location: http://py4e-data.dr-chuck.net/comments_1377120.html

Tip: find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.

'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the numbers
lst = list()
tags = soup('span')
for tag in tags:
    num = int(tag.contents[0])
    lst.append(num)
print(sum(lst))

'''
2554
'''
