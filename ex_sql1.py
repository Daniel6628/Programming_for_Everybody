'''
Counting Organizations:
This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) using a database 
with the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)

Data file : http://www.py4e.com/code3/mbox.txt.

The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, there is a balance between the number of operations you 
execute between commits and the importance of not losing the results of operations that have not yet been committed.

'''

import sqlite3
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From '):
        continue
    pieces = line.split()
    email = pieces[1]
    x = email.split('@')
    org = x[1]
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts(org, count)
                    VALUES(?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
conn.commit()
