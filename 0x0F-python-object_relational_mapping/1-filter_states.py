#!/usr/bin/python3
import MySQLdb
from sys import argv


if __name__ == "__main__":
    # Connecting to the MySQL DB
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        username=argv[1],
        password=argv[2],
        db_name=argv[3]
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
