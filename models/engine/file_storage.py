#!/usr/bin/python3

"""
class BaseModel that defines all common 
methods for other classes
"""

from models.base_model import BaseModel
from uuid import uuid4
from datetime import datetime
import json
import models

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        #__file_path = JSON.dump(__objects)
        #return to_json

    def reload(self):
        #try:
        #   my_json_object = json.dump(__objects)
        # except FileNotFoundError:
        #    pass

