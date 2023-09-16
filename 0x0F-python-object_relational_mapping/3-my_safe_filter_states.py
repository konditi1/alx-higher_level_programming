#!/usr/bin/python3
"""
 a script that takes in arguments and displays all
 values in the states table of hbtn_0e_0_usa where
 name matches the argument. But this time,
 write one that is safe from MySQL injections!
"""
import MySQLdb
import sys


def main():
    """
    List all states from the specified MySQL database.
    """
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username>"
              " <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    try:
        """ connect to the database"""
        db_connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
            charset="utf8"
        )
        """ create a cursor object to interact with the database"""
        db_cursor = db_connection.cursor()
        """ execute the SQL query to fetch states"""
        query = ("SELECT * FROM states WHERE\
                 name LIKE BINARY %s ORDER BY id ASC")
        db_cursor.execute(query, (state_name_searched,))

        """ fetch all the rows"""
        states = db_cursor.fetchall()
        """ display the results"""
        for state in states:
            print(state)
    except MySQLdb.Error as e:
        print("Error: {}".format(e))
    finally:
        """ close the cursor and the database connection"""
        db_cursor.close()
        db_connection.close()


if __name__ == "__main__":
    main()
