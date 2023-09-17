#!/usr/bin/python3
"""
script that lists all State objects from the
database hbtn_0e_6_usa
"""
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main():
    """
    List all states from the specified MySQL database
    using SQLAlchemy.
    """
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username>"
              " <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)
    # capture the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        # create database engine and connect to the database
        engine = sqlalchemy.create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                username, password, database_name
            ),
            pool_pre_ping=True
        )
        # create a session
        Session = sessionmaker(bind=engine)
        session = Session()

        # create a query to select all states
        states = session.query(State).order_by(State.id).all()

        # display the results
        for state in states:
            print("{}: {}".format(state.id, state.name))
    except sqlalchemy.DatabaseError as e:
        print(e)
    finally:
        session.close()


if __name__ == "__main__":
    main()
