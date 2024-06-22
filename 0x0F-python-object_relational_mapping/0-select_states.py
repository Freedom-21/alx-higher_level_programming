#!/usr/bin/python3
import MySQLdb
import sys


def list_states(username, password, database_name):
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query to select all states
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")

    # Fetch all the results of the query
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()


if __name__ == "__main__":
    # Get the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # List all states
    list_states(username, password, database_name)
