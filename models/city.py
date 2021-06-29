#!/usr/bin/python3
"""
class city inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    '''
    Class city which inherits from BaseModel class
    '''
    state_id = ""
    name = ""
