#!/usr/bin/python3
"""class to manage db storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """classstorage of hbnb models"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization"""
        db = 'mysql'
        dbapi = 'mysqldb'
        e_user = getenv('HBNB_MYSQL_USER')
        e_pwd = getenv('HBNB_MYSQL_PWD')
        e_host = getenv('HBNB_MYSQL_HOST')
        e_db = getenv('HBNB_MYSQL_DB')
        url = '{}+{}://{}:{}@{}/{}'.format(db, dbapi,
                                           e_user,
                                           e_pwd,
                                           e_host,
                                           e_db)
        self.__engine = create_engine(url, pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models"""
        dico = {}
        if cls is None:
            for elem in self.__session.query(State).all():
                dico[elem.__class__.__name__ + "." + elem.id] = elem
            for elem in self.__session.query(User).all():
                dico[elem.__class__.__name__ + "." + elem.id] = elem
            for elem in self.__session.query(City).all():
                dico[elem.__class__.__name__ + "." + elem.id] = elem
            for elem in self.__session.query(Amenity).all():
                dico[elem.__class__.__name__ + "." + elem.id] = elem
            for elem in self.__session.query(Place).all():
                dico[elem.__class__.__name__ + "." + elem.id] = elem
            for elem in self.__session.query(Review).all():
                dico[elem.__class__.__name__ + "." + elem.id] = elem
        else:
            for elem in self.__session.query(cls).all():
                dico[elem.__class__.__name__ + "." + elem.id] = elem
        return dico

    def new(self, obj):
        """Adds new object"""
        self.__session.add(obj)

    def delete(self, obj=None):
        """Delete obj"""
        if obj is None:
            return
        self.__session.delete(obj)

    def save(self):
        """Saves"""
        self.__session.commit()

    def reload(self):
        """Loads tables"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Call remove() method on the private session attribute
           or close() on the class Session"""
        self.__session.close()
