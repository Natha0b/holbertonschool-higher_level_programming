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
    matchName = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities\
                JOIN states \
                    ON cities.state_id = states.id\
                WHERE states.name=%s\
                ORDER by cities.id ASC", (matchName,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(','.join(row))
    cur.close()
    conn.close()
