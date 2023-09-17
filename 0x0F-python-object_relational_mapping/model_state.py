#!/usr/bin/python3
"""Define a State class and create the states table in a MySQL database."""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL for Connecting to the database
DATABASE_URI = 'mysql://papa:2222@localhost/hbtn_0e_6_usa'

Base = declarative_base()


class State(Base):
    """State class representing the states table."""

    __tablename__ = 'states'

    id = Column("id",
                Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True
                )
    name = Column("name", String(128), nullable=False)


def main():
    # Create the database engine and bind it to the Base.
    engine = create_engine(DATABASE_URI, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Optionally, you can add data to the table here using SQLAlchemy sessions.
    # Session = sessionmaker(bind=engine)
    # session = Session()
    # new_state = State(name="New York")
    # session.add(new_state)
    # session.commit()
    # session.close()


if __name__ == "__main__":
    main()
