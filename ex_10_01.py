'''
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the
messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using
a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. Note that the autograde
r does not have support for the sorted() function.
'''

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
lst = list()
for lines in handle:
    if not lines.startswith('From'):
        continue
    lines = lines.rstrip()
    words = lines.split()
    if len(words) < 5:                 #some lines starting with 'From' doesn't include time
        continue
    time = words[5]
    hour = time.split(':')
    lst.append(hour[0])
    
for hr in lst:                         #make a dictionary ('histogram')
    counts[hr] = counts.get(hr, 0) + 1
    
for k,v in sorted(counts.items()) :    #sorted(counts.items()) gives us a sorted list of tuples, i.e. [(),(),()..]
    print(k,v)                         #also note that tuples are comparable hence they can be sorted
