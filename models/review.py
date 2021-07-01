#!/usr/bin/python3
from models.base_model import BaseModel

class Review(BaseModel):
	"""
	This class inherits from base models
	three public attributes are created
	"""
	place_id = ""
	user_id = ""
	text = ""
