#!/usr/bin/python3
"""
This is base_model module
Contains thc BaseModel class
"""

from datetime import datetime
import uuid
import models

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """The Basemodel class from which future classes will be derived"""
    
    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    
    def __str__(self):
        """Returns a string representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)
