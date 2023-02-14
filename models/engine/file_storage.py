#!/usr/bin/python3

"""

The FileStorage class model

"""

import json

from os.path import exists


# from models.base_model import BaseModel


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

        with open(self.__file_path, mode="w+") as jsonfile:

            dict_storage = {}

            for k, v in self.__objects.items():

                dict_storage[k] = v.to_dict()

            json.dump(dict_storage, jsonfile)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """

        if exists(self.__file_path):
            """
            deserializes the JSON file to __objects, if the json file
            exists, else do nothing
            """
            try:
                with open(self.__file_path, 'r') as jsonfile:
                    dict = json.loads(jsonfile.read())
                    for value in dict.values():
                        cls = value["__class__"]
                        self.new(eval(cls)(**value))
            except Exception:
                pass
