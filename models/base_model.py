#!/bin/usr/python3

import uuid
import datetime

"""
    Base model for all other classes
    defines all common attributes/methods for other classes
"""


def dateTime():
    return datetime.datetime.now().isoformat()


class BaseModel:
    """Class BaseModel"""

    def __init__(self):
        """
            initializes the base model with unique id generated with uuid
            date the instance is created, date it is modified
        """
        self.id = str(uuid.uuid4())
        self.created_at = dateTime()
        self.updated_at = dateTime()

    def save(self):
        """
            Instance method
            saves/updates the created object instance
        """
        self.updated_at = dateTime()

    def to_dict(self):
        """
            returns a dictionary containing all 
            keys/values of __dict__ of the instance
        """
        self['__class__'] = self.__class__.__name__
        return self.__dict__
