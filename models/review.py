#!/usr/bin/python3
"""
review.py
Review Class
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    It's a child class of BaseModel
    It'll be a review of the Airbnb
    """

    place_id = ""
    user_id = ""
    text = ""
