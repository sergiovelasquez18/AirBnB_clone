#!/usr/bin/python3
"""

"""
import uuid
from datetime import datetime

class BaseModel():
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        my_dict = self.__dict__
        my_dict['__class__'] = self.__class__.__name__
        return my_dict


if __name__=='__main__':
    model1 = BaseModel()
    model1.name = "Holbie"
    model1.mynumber = 89
    print(model1)
    print("//////////////////////////////////////////////////////////")
    model1.save()
    print(model1)
    print("//////////////////////////////////////////////////////////")
    my_model_json = model1.to_dict()
    print(my_model_json)