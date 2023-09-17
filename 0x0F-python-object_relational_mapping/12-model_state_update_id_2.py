#!/usr/bin/python3
"""
script that changes the name of a State object from
the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
     changes the name of a State object from the
     database hbtn_0e_6_usa
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
        state = session.query(State).order_by(State.id).all()
        # display the results
        for state in state:
            if state.id == 2:
                state.name = "New Mexico"
            session.commit()
    except sqlalchemy.exc.DatabaseError as e:
        print(e)
    finally:
        session.close()


if __name__ == "__main__":
    main()
