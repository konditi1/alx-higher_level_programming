#!/usr/bin/python3
"""
This script lists all states from the specified MySQL database.

Usage:
    ./script_name.py <mysql_username> <mysql_password> <database_name>

Arguments:
    mysql_username (str): The MySQL username.
    mysql_password (str): The MySQL password.
    database_name (str): The name of the database to connect to.
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username>"
              " <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name,
            charset="utf8"
        )

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Execute the SQL query to fetch states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all the rows
        states = cursor.fetchall()

        # Display the results
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("Error connecting to the database or executing the query: {}".format(e))
    finally:
        # Close the cursor and the database connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()
