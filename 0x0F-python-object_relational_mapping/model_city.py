#!/usr/bin/python3
"""Define a State class and create the states table in a MySQL database."""
import sys
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from model_state import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL for Connecting to the database
DATABASE_URI = 'mysql://papa:2222@localhost/hbtn_0e_14_usa'


class City(Base):
    """State class representing the states table."""

    __tablename__ = 'cities'

    id = Column("id",
                Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True
                )
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", Integer, ForeignKey("states.id"))


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
