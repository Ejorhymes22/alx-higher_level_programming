#!/usr/bin/python3
""" this lists all cities from a database"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM states INNER JOIN cities ON cities.state_id=states.id")

    dblist = cur.fetchall()
    for i in dblist:
        print(i)

    cur.close()
    db.close()
