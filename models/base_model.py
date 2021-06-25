#!/usr/bin/python3

import uuid
import datetime


class BaseModel():

    def __init__(self):
        '''
        * created_at: assign with the current datetime when an instance is created
        * updated at: assign with the current datetime when an instance is created
        and it will be updated every time you change your object
        * id: assign with an uuid when an instance is created
        '''
        self.created_at = str(datetime.datetime.strptime(
            '2016-10-06 15:14:54.322989', '%Y-%m-%d %H:%M:%S.%f'))
        self.updated_at = str(datetime.datetime.strptime(
            '2016-10-06 15:14:54.322989', '%Y-%m-%d %H:%M:%S.%f'))
        self.id = str(uuid.uuid4())

    def __str__(self):
        '''str magic method returns the characteristics of the object'''
        return ("[{}] ( {} {})".format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        '''updates the public instance attribute updated_at with the current datetime'''
        self.updated_at = str(datetime.datetime.strptime(
            '2016-10-06 15:14:54.322989', '%Y-%m-%d %H:%M:%S.%f'))
        print("HOLAHOLAHOLA: {}".format(self.updated_at))

    def to_dict(self):
        '''returns a dictionary containing all keys/values of __dict__ of the instance'''
        return self.__dict__

my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key,
          type(my_model_json[key]), my_model_json[key]))





