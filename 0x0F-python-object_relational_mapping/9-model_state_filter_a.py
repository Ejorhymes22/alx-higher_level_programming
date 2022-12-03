#!/usr/bin/python3
"""lists all object that contains the letter a"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys

if __name__ == "__main__":
    session = sessionmaker()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session.configure(bind=engine)

    dbsession = session()
    listState = dbsession.query(State).filter(State.name.op('regexp')('a'))
    for q in listState:
        print("{}: {}".format(q.id, q.name))
