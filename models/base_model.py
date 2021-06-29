#!/usr/bin/python3

import uuid
from datetime import datetime
import models


class BaseModel():

    def __init__(self, *args, **kwargs):
        '''
        * created_at: assign with the current datetime when
        an instance is created
        * updated at: assign with the current datetime when
        an instance is created
        and it will be updated every time you change your object
        * id: assign with an uuid when an instance is created
        '''
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    pass
                elif key == 'created_at':
                    self.created_at = datetime.strptime(
                                                value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(
                                                value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    setattr(self, key, value)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            models.storage.new(self)

    def __str__(self):
        '''str magic method returns the characteristics of the object'''
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                       self.id, self.__dict__)

    def save(self):
        '''
        updates the public instance attribute updated_at with
        the current datetime
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        '''
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = str(self.created_at.isoformat())
        new_dict["updated_at"] = str(self.updated_at.isoformat())
        new_dict["__class__"] = self.__class__.__name__
        return new_dict