#!/usr/bin/python3
"""
script that takes in the name of a state as an
argument and lists all cities of that state,
using the database hbtn_0e_4_usa
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
    state_name = sys.argv[4]

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
        query = "SELECT cities.name\
                  FROM cities JOIN states ON\
                  cities.state_id = states.id\
                  WHERE states.name = %s\
                  ORDER BY cities.id ASC"
        db_cursor.execute(query, (state_name,))
        """ fetch all the rows"""
        cities = db_cursor.fetchall()
        """ display the results"""
        conc_city = ""
        for city in cities:
            conc_city += city[0] + ", "
        print(conc_city[:-2])

    except MySQLdb.Error as e:
        print("Error: {}".format(e))
    finally:
        """ close the cursor and the database connection"""
        db_cursor.close()
        db_connection.close()


if __name__ == "__main__":
    main()
