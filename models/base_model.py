#!/usr/bin/python3

"""
class BaseModel that defines all common
methods for other classes
"""

from uuid import uuid4
from datetime import datetime
import json
import models


class BaseModel:
    """
    class BaseModel for the common methods
    """
    def __init__(self, *args, **kwargs):
        """Initialize class base
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value,
                                                  "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        public instance to print name, id, dict
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
        updates the public instance attribute with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()


    def to_dict(self):
        """dictionary with the values

        Returns:
        [dict]: [containing all keys/values ]
        """
        # se trabaja es con una copia del diccionario
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
