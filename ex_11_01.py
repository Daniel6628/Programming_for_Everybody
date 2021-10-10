'''
Finding Numbers in a Haystack

Handling The Data
The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' 
and then converting the extracted strings to integers and summing up the integers.

The file can be found [here](http://py4e-data.dr-chuck.net/regex_sum_1377118.txt)
'''


import re
hand = open('regex_sum_1377118.txt')
lst = list()
count = 0

for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    num = [int(i) for i in stuff]
    nums = sum(num)
    lst.append(nums)
print(sum(lst))
