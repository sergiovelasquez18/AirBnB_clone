#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
	"""
	This class inherits from base models
	four public attributes are created
	"""
	email = ""
	password = ""
	first_name = ""
	last_name = ""