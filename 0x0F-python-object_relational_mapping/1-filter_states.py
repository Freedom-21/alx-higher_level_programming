#!/usr/bin/python3
import MySQLdb
import sys


def filter_states(username, password, database_name):
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

    # Execute the SQL query to select states with names starting with 'N'
    cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the results of the query
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
#!/usr/bin/python3
import MySQLdb
from sys import argv


if __name__ == '__main__':
    # Connecting to the MySQL DB
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        username=argv[1],
        password=argv[2],
        db_name=argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    # Get the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # List all states with names starting with 'N'
    filter_states(username, password, database_name)
