#!/usr/bin/python3
"""
class User inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    '''
    Class User which inherits from BaseModel class
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
