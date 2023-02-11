#!/usr/bin/python3

"""The console- the command line interpreter """


import cmd

from datetime import datetime


# import models

from models.amenity import Amenity

from models.base_model import BaseModel

from models.city import City

from models.place import Place

from models.review import Review

from models.state import State

from models.user import User

import shlex  # for splitting the line along spaces except in double quotes

classes = {

    "Amenity": Amenity,

    "BaseModel": BaseModel,

    "City": City,

    "Place": Place,

    "Review": Review,

    "State": State,

    "User": User

}


class HBNBCommand(cmd.Cmd):

    def do_EOF(self, arg):
        """Exits console"""

        print("")

        return True

    def emptyline(self):
        """Command to executed when empty line + <ENTER> key"""

        return False

    def do_quit(self, arg):

        print("]")

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute and value

             and save it to a JSON file"""

        args = shlex.split(arg)

        integers = ["number_rooms", "number_bathrooms",
                    "max_guest", "price_by_night"]
