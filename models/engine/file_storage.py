#!/usr/bin/python3

"""

Contains the FileStorage class model

"""

import json

from os.path import exists


from models.base_model import BaseModel

from models.user import User

from models.state import State

from models.amenity import Amenity

from models.city import City

from models.place import Place

from models.review import Review


class FileStorage:

    """

    serializes instances to a JSON file and

    deserializes JSON file to instances

    """


    __file_path = "file.json"

    __objects = {}


    def all(self):

        """

        Returns the dictionary __objects

        """

        return self.__objects


    def new(self, obj):

        """

        sets in __objects the `obj` with key <obj class name>.id

        """

        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj


    def save(self):

        """

        Serialize __objects to the JSON file

        """

        with open(self.__file_path, mode="w") as jsonfile:

            dict_storage = {}

            for k, v in self.__objects.items():

                dict_storage[k] = v.to_dict()

            json.dump(dict_storage, jsonfile)


    def reload(self):

        """deserializes the JSON file to __objects"""

        

        if exists(self.__file_path):

            with open(self.__file_path) as jsonfile:

                decereal = json.load(jsonfile)

            for keys in decereal.keys():

                if decereal[keys]['__class__'] == "BaseModel":

                    self.__objects[keys] = BaseModel(**decereal[keys])

                elif decereal[keys]['__class__'] == "User":

                    self.__objects[keys] = User(**decereal[keys])

                elif decereal[keys]['__class__'] == "State":

                    self.__objects[keys] = State(**decereal[keys])

                elif decereal[keys]['__class__'] == "City":

                    self.__objects[keys] = City(**decereal[keys])

                elif decereal[keys]['__class__'] == "Amenity":

                    self.__objects[keys] = Amenity(**decereal[keys])

                elif decereal[keys]['__class__'] == "Place":

                    self.__objects[keys] = Place(**decereal[keys])

                elif decereal[keys]['__class__'] == "Review":

                    self.__objects[keys] = Review(**decereal[keys])
