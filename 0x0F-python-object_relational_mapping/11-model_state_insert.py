#!/usr/bin/python3
"""
script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
"""
import sys
import sqlalchemy
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    connect to MySQL server through the args
    and print new states.id
    """
    if len(sys.argv) != 4:
        print("few arguments")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        # connect to the engine and to the database
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database_name
        ), pool_pre_ping=True)

        # create a session
        Session = sessionmaker(bind=engine)
        session = Session()

        # create a new state object with the name 'Louisiana'
        louisiana_state = State(name="Louisiana")

        # add the new State object to the session
        session.add(louisiana_state)

        # commit the transaction to save the new state to the database
        session.commit()
        print(louisiana_state.id)
    except sqlalchemy.exc.DatabaseError as e:
        print(e)
    finally:
        session.close()


if __name__ == "__main__":
    main()
