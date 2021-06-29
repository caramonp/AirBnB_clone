#!/usr/bin/python3
"""
class Review inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    '''
    Class Review which inherits from BaseModel class
    '''
    place_id = ""
    user_id = ""
    text = ""
