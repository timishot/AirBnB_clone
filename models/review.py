#!/usr/bin/python3
"""Define the review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent class"""

    place_id = ""
    user_id = ""
    text = ""
