'''
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, 
the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

#IMPORTANT: create a list for later use
lst = list()
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    words = line.split()
    #collect all the 2nd element in a list so that they can be picked to make a dictionary later
    lst.append(words[1])
    
    counts = dict()
    #make a 'histogram' in dictionary
    for word in lst:
        counts[word] = counts.get(word, 0) + 1
#calculate the max (align with the 1st 'for' loop)    
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
