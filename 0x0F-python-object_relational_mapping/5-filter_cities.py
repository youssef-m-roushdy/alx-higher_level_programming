#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT DISTINCT cities.name FROM cities "
                + "INNER JOIN states ON cities.state_id = states.id "
                + "WHERE states.name = %s", (sys.argv[4],))
    rows = cur.fetchall()
    cities = [row[0] for row in rows]
    print(", ".join(cities))
    cur.close()
    db.close()
