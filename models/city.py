#!/usr/bin/python3
"""Module for city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This class inherits from base models
    two public attributes are created
    """
    state_id = ""
    name = ""
