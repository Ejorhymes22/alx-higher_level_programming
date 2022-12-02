#!/usr/bin/python3
"""selecting stayes using sqlalchemy"""

import MySQLdb
import sys


db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
myresult = cur.fetchall()
for i in myresult:
    print(i)

cur.close()
db.close()
