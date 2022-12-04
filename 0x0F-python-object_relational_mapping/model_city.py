#!/usr/bin/python3
"""contains the class definition of a City"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """This inherits from Base
    has id and name
    as well as foriegn
    key"""

    __tablename__ = "cities"

    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State")
