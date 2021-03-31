#!/usr/bin/python3
""" Place Module for HBNB project """

import models
from models.base_model import BaseModel, Base
# from models.city import City
from models.user import User
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class Place(BaseModel, Base):
    """ A place to stay """
    if models.storage_type == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship(
                "Review", backref="place", cascade="all, delete")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    if models.storage_type != 'db':
        @property
        def reviews(self):
            """Getter returns the list of Review instances
            - with the place_id = Place.id"""
            list_reviews = []
            # all: returns a dictionary of models currently in FileStorage"""
            all_reviews = models.storage.all(Place)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    list_reviews.append(review)
            return list_reviews

    def __init__(self, *args, **kwargs):
        """Initializing of the Place object"""
        super().__init__(*args, **kwargs)
