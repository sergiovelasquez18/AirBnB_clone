#!/usr/bin/python3

import json


class FileStorage():


    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionar representation of __objects"""
        print (FileStorage.__objects)
        print (self.__objects)
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, mode="w", encoding="UTF8") as my_file:
                json.dump(self.__objects, my_file)
        if self.__objects:
            print("OBJECTS EXISTE \n")
        else:
            print("NO EXISTE")

    def reload(self):
        """"
        deserializes the JSON file to __objects(only if the
        JSON file(__file_path) exists otherwise, do nothing.
        If the file doesn’t exist, no exception will be raised)
        """
        try:
            with open(self.__file_path, mode="r", encoding="UTF8") as my_file:
                    return json.load(my_file)
        except:
            pass





