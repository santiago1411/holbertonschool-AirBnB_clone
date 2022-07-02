#!/usr/bin/python3

"""Module for Filestorage"""
import json
from os import path

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
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Method that serializes __objects to the JSON file"""

        with open(self.__file_path, "w", encoding = 'utf-8') as file:
            serial = json.dumps(self.__objects, sort_keys=True, default=str)
            file.write(serial)


    def reload(self):
        if path.exists(self.__file_path):
            with open(self.__file_path, "r") as r:
                self.__objects = json.loads(r.read())
