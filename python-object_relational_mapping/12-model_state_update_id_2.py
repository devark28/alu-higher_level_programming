#!/usr/bin/python3
"""
Module to get all states
"""
from sys import argv

from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    username, password, database = argv[1:4]
    # default host is 'localhost' and default port is '3306'
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, database),
        pool_pre_ping=True
    )
    session = Session(engine)
    Base.metadata.create_all(engine)

    state = session.query(State).filter(State.id == 2).first()
    session.name = "New Mexico"
    session.commit()
    # print(f"{state.id}")

    session.close()
