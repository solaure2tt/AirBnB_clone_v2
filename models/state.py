#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from models.city import City
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb
import shlex
from os import getenv
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", cascade='all, delete, delete-orphan',
                              backref="state")
    else:
        @property
        def cities(self):
            cities = []
            tmp = []
            for key in models.storage.all():
                ci = key.replace('.', ' ')
                city = shlex.split(ci)
                if (city[0] == 'City'):
                    ms = models.storage.all()
                    tmp.append(ms[key])
            for obj in tmp:
                if (obj.state_id == self.id):
                    cities.append(obj)
            return (cities)
