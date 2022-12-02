#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import MySQLdb


    db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    stateName=sys.argv[4]
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities WHERE cities.state_id=(SELECT id FROM states WHERE states.name=%s)", [stateName])
    l = cur.fetchall()

    z = 1
    for i in l:
        k = ''
        for j in i:
            k += j
        if (z == 1):
            print(k, end="")
        else:
            print(", ", k, end="")
        z += 1
    print()
