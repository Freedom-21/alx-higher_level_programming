#!/usr/bin/python3
import MySQLdb
import sys


def filter_states(username, password, db_name):
    # Connecting to the MySQL DB
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cur = db.cursor()
    cur.execute(
        "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

    if __name__ == "__main__":
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]

        filter_states(username, password, db_name)
