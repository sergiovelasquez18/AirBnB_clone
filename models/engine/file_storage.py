#!/usr/bin/python3

import json
from models.base_model import BaseModel

class FileStorage:


    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionar representation of __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_file = {}
        for key in self.__objects:
            json_file[key] = self.__objects[key].to_dict()
        with open(self.__file_path, mode="w", encoding="UTF8") as my_file:
                json.dump(json_file, my_file)

    def reload(self):
        """"
        deserializes the JSON file to __objects(only if the
        JSON file(__file_path) exists otherwise, do nothing.
        If the file doesn’t exist, no exception will be raised)
        """
        try:
            with open(self.__file_path, mode="r", encoding="UTF8") as my_file:
                    return json.load(self.__objects)
        except:
            pass





