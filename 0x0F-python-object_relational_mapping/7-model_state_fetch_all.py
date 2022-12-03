#!/usr/bin/python3
"""lists all the state objects from the database"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys

if __name__ == "__main__":
    Session = sessionmaker()

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(bind=engine)
    Session.configure(bind=engine)

    DBSession = Session()
    stateList = DBSession.query(State)
    for state in stateList:
        print("{}: {}".format(state.id, state.name))
