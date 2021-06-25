#!/usr/bin/python3

import uuid
import datetime

class BaseModel():

    def __init__(self, id, created_at, updated_at):
        self.created_at = datetime.datetime.strptime(
            '2020-06-19T15:52:50Z', "%Y-%m-%dT%H:%M:%SZ")
        self.updated_at = datetime.datetime.strptime(
            '2020-06-19T15:52:50Z', "%Y-%m-%dT%H:%M:%SZ")
        self.id = str(uuid.uuid4())

    def __str__(self):
        '''str magic method returns the characteristics of the object'''
        return ("[{}] ( {} {})".format(type(self).__name__, self.id, self.__dict__))


my_model = BaseModel(5, 5, 5)
print(my_model.id)
print(my_model.created_at)
print(my_model.updated_at)
print(my_model)




