#!/usr/bin/python3
"""lists all the state objects from the database"""
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from zope.sqlalchemy import ZopeTransactionExtension
from model_state import Base, State
import sys

if __name__ == "__main__":
    DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
    stateList = DBSession.query(State)
    for state in stateList:
        print(state.name)



    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

