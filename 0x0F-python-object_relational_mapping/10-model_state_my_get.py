#!/usr/bin/python3
"""
 script that prints the State object with the name
 passed as argument from the database hbtn_0e_6_usa
"""
import sys
import sqlalchemy
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    """
    List all states from the specified MySQL database
    using SQLAlchemy.
    """
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username>"
              " <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_to_search = sys.argv[4]

    try:
        # create database engine and connect to the database
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database_name),
                               pool_pre_ping=True)
        # create a session
        Session = sessionmaker(bind=engine)
        session = Session()
        # create a query to select all states
        state = session.query(State)
        state = state.filter(State.name == state_name_to_search).first()
        # display the results
        if state is None:
            print("Not found")
        else:
            print("{}".format(state.id))
    except sqlalchemy.exc.DatabaseError as e:
        print(e)
    finally:
        session.close()


if __name__ == "__main__":
    main()
