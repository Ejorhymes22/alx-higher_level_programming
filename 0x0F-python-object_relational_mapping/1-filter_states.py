#!/usr/bin/python3
"""selecting by state that start with N"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name regexp '^N.*' ORDER BY id ASC")
    mylist = cur.fetchall()
    for i in mylist:
        print(i)

    cur.close()
    db.close()
