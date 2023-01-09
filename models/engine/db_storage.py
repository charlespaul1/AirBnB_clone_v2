#!usr/bin/python3
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects in the database"""
        objects = {}
        if cls:
            for obj in self.__session.query(cls).all():
                key = obj.__class__.__name__ + '.' + obj.id
                objects[key] = obj
        else:
            for class_name in ['User', 'State', 'City', 'Amenity',
                               'Place', 'Review']:
                cls = eval(class_name)
                for obj in self.__session.query(cls).all():
                    key = obj.__class__.__name__ + '.' + obj.id
                    objects[key] = obj
        return objects

    def new(self, obj):
        """Add the object to the database"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete the object from the database"""
        if obj:
            self.__session.delete(obj)
        self.session.commit()

    def reload(self):
        """
        Create all tables in the database and create the current database
        session.
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False))
