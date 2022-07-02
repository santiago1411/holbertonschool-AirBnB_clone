#!/usr/bin/python3

"""Module for Filestorage"""
import json
from os import path

class Filestorage:
    """Class Filestorage
    to serialize and deserialize files into and
    """

    __file_path = ".__name__ + .json"
    __objects = {}

    def __init__(self):
        """Class constructor"""

    def all(self):
        return self.__objects
    
    def new(self, obj)

    def save(self)
        with open(self.__file_path, "w") as write:
            json.dumb(self.__objects, write)

    def reload(self):
        if path.exists(self.__name__ + ".json"):
            data = json.loads(self.__name__ + ".json")
        return(data)
