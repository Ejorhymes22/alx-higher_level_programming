#!/usr/bin/python3
"""prints out the first State"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys


if __name__ == "__main__":
    Session = sessionmaker()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session.configure(bind=engine)

    dbsession = Session()
    query = dbsession.query(State)

    print("{}: {}".format(query[0].id, query[0].name))
