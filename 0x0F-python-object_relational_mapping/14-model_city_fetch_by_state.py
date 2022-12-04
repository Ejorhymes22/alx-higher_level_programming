#!/usr/bin/python3
"""prints all citys objects from the database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    session = sessionmaker()
    session.configure(bind=engine)

    dbsession = session()
    query = dbsession.query(City).join(State)\
                     .filter(City.state_id == State.id).all()
    for row in query:
        print("{}: ({}) {}".format(row.state.name, row.id, row.name))
