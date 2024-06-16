#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Creates a new user to the database
        """
        neu_user = User(email=email, hashed_password=hashed_password)
        self._session.add(neu_user)
        self._session.commit()
        return neu_user

    def find_user_by(self, **kwargs) -> User:
        """Finds a user in the database"""
        try:
            user = self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise ValueError("Not found")
        except InvalidRequestError:
            raise ValueError("Invalid")
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Updates a user details"""
        try:
            user = self.find_user_by(id=user_id)
        except NoResultFound:
            raise ValueError("Not found")

        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
            else:
                raise ValueError(
                    f"Attribute '{key}' does not exist")

        self._session.commit()
