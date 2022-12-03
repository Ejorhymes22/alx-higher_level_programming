#!/usr/bin/python3
"""This creates a class state"""
import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                       sys.argv[2], sys.argv[3]), pool_pre_ping=True)
Base = declarative_base()


class State(Base):
    """States of America
    inherits from Base
    links to the states
    unique integer
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128))


Base.metadata.create_all(engine)
