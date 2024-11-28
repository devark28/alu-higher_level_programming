#!/usr/bin/python3
"""
Module to get all states
"""
from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from model_state import State

if __name__ == "__main__":
    username, password, database = argv[1:4]
    # default host is 'localhost' and default port is '3306'
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, database)
    )
    session = Session(engine)

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
