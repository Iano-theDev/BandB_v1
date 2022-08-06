#!/usr/bin/python3

"""
user.py
user class

"""

from models.base_model import BaseModel

class user(Basemodel):
    """
    This is a BaseModel child class
    It contains information about the user's identity
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
