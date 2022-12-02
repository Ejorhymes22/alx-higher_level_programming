#!/usr/bin/python3
"""selecting a particular state"""
import sys
import MySQLdb


db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
element = sys.argv[4];
cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", [element])
listcur = cur.fetchone()
print(listcur)


cur.close()
db.close()
