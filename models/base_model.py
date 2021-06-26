#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel():

    def __init__(self, *args, **kwargs):
        '''
        * created_at: assign with the current datetime when an instance is created
        * updated at: assign with the current datetime when an instance is created
        and it will be updated every time you change your object
        * id: assign with an uuid when an instance is created
        '''
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if(key == '__class__'):
                    pass
                elif(key == 'created_at'):
                    self.created_at = datetime.strptime(
                    value, '%Y-%m-%dT%H:%M:%S.%f')
                elif(key == 'updated_at'):
                    self.updated_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    setattr(self, key, value)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())


    def __str__(self):
        '''str magic method returns the characteristics of the object'''
        return ("[{}] ( {} {})".format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        '''updates the public instance attribute updated_at with the current datetime'''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' returns a dictionary containing all keys/values of __dict__ of the instance'''
        return {'my_number': self.my_number,
                'name': self.name,
                '__class__': self.__class__.__name__,
                'updated_at': str(self.updated_at.isoformat()),
                'id': self.id,
                'created_at': str(self.created_at.isoformat())}

    def create(cls, **dictionary):
        '''returns an instance with all attributes already set'''
        temp_inst = cls(1)
        a_inst.update(**dictionary)
        return temp_inst


my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key,
          type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)





