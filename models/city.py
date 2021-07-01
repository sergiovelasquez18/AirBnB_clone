#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """
    This class inherits from base models
    two public attributes are created
    """
    state_id = ""
    name = ""
