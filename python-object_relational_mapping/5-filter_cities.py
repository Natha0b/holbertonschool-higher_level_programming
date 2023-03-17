#!/usr/bin/python3
"""
Third MySQLdb script
"""


import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    matchName = sys.argv[4].split(';')[0].strip("'")

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                WHERE states.name=%s \
                ORDER BY cities.id ASC", (matchName,)
                )
    query_rows = cur.fetchall()
    cities = []
    for row in query_rows:
        cities.append("{}".format(row[0]))
    print(", ".join(cities))
    cur.close()
    conn.close()
