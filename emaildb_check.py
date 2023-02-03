import sqlite3

conn = sqlite3.connect('ahnskdb.sqlite')
cur = conn.cursor()

sqlstr = 'SELECT * FROM Counts'

domain_dic = {}

for row in cur.execute(sqlstr):
    domain = row[0].split('@')[1]
    if domain in domain_dic:
        domain_dic[domain] = domain_dic[domain] + row[1]
    else:
        domain_dic[domain] = row[1]

cur.execute('DROP TABLE Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
for k, v in sorted(domain_dic.items(), key=(lambda item: item[1]), reverse=True):
    cur.execute('INSERT INTO Counts (org, count) VALUES (?, ?)', (k, v))
    conn.commit()
    print(k, v)