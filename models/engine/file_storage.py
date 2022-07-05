#!/usr/bin/python3

"""Module for Filestorage"""
import json
from os.path import exists
from models.user import User
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.place import Place

class Filestorage:
    """Class Filestorage
    to serialize and deserialize files into and
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Class constructor"""

    def all(self):
        return self.__objects
    
    def new(self, obj):
        """
        Method that sets the obj in __objects
        with key <obj class name>.id
        """
        obj2 = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[obj2] = obj

    def save(self):
        """Method that serializes __objects to the JSON file"""

        with open(self.__file_path, "w", encoding = 'utf-8') as file:
            serial = json.dumps(self.__objects, sort_keys=True, default=str)
            file.write(serial)


    def reload(self):
        if exists(self.__file_path):
            with open(self.__file_path, "r") as r:
                self.__objects = json.loads(r.read())
