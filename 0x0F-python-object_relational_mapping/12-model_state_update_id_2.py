#!/usr/bin/python3
"""changes the name of a state object"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    dbsession = sessionmaker()
    dbsession.configure(bind=engine)

    session = dbsession()
    x = session.query(State).get(2)
    x.name = 'New Mexico'
    session.commit()
