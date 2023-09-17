#!/usr/bin/python3
"""
script that prints the first State object from the
database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    """
    List all states from the specified MySQL database
    using SQLAlchemy.
    """
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username>"
              " <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        # create database engine and connect to the database
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database_name),
                               pool_pre_ping=True)
        # create a session
        Session = sessionmaker(bind=engine)
        session = Session()
        # create a query to select all states
        states = session.query(State).order_by(State.id).first()
        # display the results
        if states is None:
            print("Nothing")
        else:
            print("{}: {}".format(states.id, states.name))

    except sqlalchemy.DatabaseError as e:
        print(e)
    finally:
        session.close()


if __name__ == "__main__":
    main()
