#!/usr/bin/python3
"""
script that lists all states with a name starting with
N (upper N)from the database hbtn_0e_0_usa:
"""
import MySQLdb
import sys


def main():
    """
    List all states from the specified MySQL database.
    """
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username>"
              " <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    passwrd = sys.argv[2]
    db_name = sys.argv[3]

    try:
        """ connect to the database"""
        db_connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=passwrd,
            db=db_name,
            charset="utf8"
        )
        """ create a cursor object to interact with the database"""
        db_cursor = db_connection.cursor()
        """ execute the SQL query to fetch states"""
        db_cursor.execute("SELECT * FROM states ORDER BY id ASC")
        """ fetch all the rows"""
        states = db_cursor.fetchall()
        """ display the results"""
        for state in states:
            if state[1][0] == 'N':
                print(state)
    except MySQLdb.Error as e:
        print("Error: {}".format(e))
    finally:
        """ close the cursor and the database connection"""
        db_cursor.close()
        db_connection.close()


if __name__ == "__main__":
    main()
