#!/usr/bin/python3
"""
script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
import sqlalchemy


def main():
    """
    deletes all State objects with a name
    containing the letter a from the database hbtn_0e_6_usa
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
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database_name
        ),
            pool_pre_ping=True)
        # create a session
        Session = sessionmaker(bind=engine)
        session = Session()
        # Delete states with names containing 'a' directly in the SQL query
        session.query(State).filter(State.name.like('%a%')).delete()

        # Commit the transaction to save the changes to the database
        session.commit()

    except sqlalchemy.exc.DatabaseError as e:
        print(e)
    finally:
        session.close()


"""
           # create a query to select all states
        states = session.query(State).order_by(State.id).all()
        # display the results
        for state in states:
            if state.name.__contains__("a"):
                session.delete(state)
        session.commit()
"""


if __name__ == "__main__":
    main()
