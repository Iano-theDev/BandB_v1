#!/usr/bin/python3
"""
city.py
city class
"""

from models.base_model import BaseModel
    
class City(BaseModel):
    """
    It is a child class of BaseModel
    Contains information about the cities' identity
    """

    state_id = ""
    name = ""
