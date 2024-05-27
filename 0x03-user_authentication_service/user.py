#!usr/bin/env python3
'''Module implements the User class'''
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    '''Implementation of the User model class'''
    __tablename__ = 'users'

    id = Column(Integer(60), primary_key=True)
    email = Column(String(128), nullable=False)
    hashed_password = Column(String(128), nullable=False)
    session_id = Column(String(128), nullable=True)
    reset_token = Column(String(128), nullable=True)
