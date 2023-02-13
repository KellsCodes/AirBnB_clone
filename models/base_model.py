#!/bin/usr/python3

import uuid
from datetime import datetime
import models

"""
Base model for all other classes
defines all common attributes/methods for other classes
"""


def dateTime():
    return datetime.utcnow()


class BaseModel:
    """Class BaseModel"""

    def __init__(self, *args, **kwargs):
        """
        initializes the base model with unique id generated with uuid
        date the instance is created, date it is modified
        """
        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = dateTime()
            self.updated_at = dateTime()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                        value, DATE_TIME_FORMAT)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def save(self):
        """
        Instance method
        saves/updates the created object instance
        """
        self.updated_at = dateTime()
        models.storage.save(self)

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        my_obj = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                my_obj[key] = value.isoformat()
            else:
                my_obj[key] = value

        my_obj['__class__'] = self.__class__.__name__
        return my_obj
