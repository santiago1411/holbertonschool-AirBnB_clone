#!/usr/bin/python3

"""module"""
import models
import uuid
from datetime import datetime


class BaseModel:

    """Class BaseModel
    Attr:
    __nb_objects: number instance
    """
    name = ""
    my_number = 0

    def __init__(self, *args, **kwargs):
        """initiliazes an instance"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    dt_obj = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, dt_obj)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        Dictionary = self.__dict__.copy()
        Dictionary["__class__"] = self.__class__.__name__
        Dictionary["created_at"] = self.created_at.isoformat()
        Dictionary["updated_at"] = self.updated_at.isoformat()
        return (Dictionary)
