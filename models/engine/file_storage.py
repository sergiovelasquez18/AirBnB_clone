#!/usr/bin/python3

import json
from models.base_model import BaseModel


class FileStorage():

    __file_path = "file.json"
    __objects = {}

    def all(FileStorage):
        """
        Returns the dictionar representation of __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        tmp_dic = {}
        for key in self.__objects:
            tmp_dic[key] = self.__objects[key].to_dict()
        with open(FileStorage.__file_path, mode="w",
                  encoding="UTF8") as my_file:
                json.dump(tmp_dic, my_file)

    def reload(self):
        """"
        deserializes the JSON file to __objects(only if the
        JSON file(__file_path) exists otherwise, do nothing.
        If the file doesn’t exist, no exception will be raised)
        """
        try:
            with open(FileStorage.__file_path, mode="r",
                      encoding="UTF8") as my_file:
                tmp_obj = json.load(my_file)
            for keys in tmp_obj.keys():
                class_obj = keys.split('.')
                obj = class_obj[0] + "(**tmp_obj[keys])"
                self.__objects[keys] = eval(obj)
        except:
            pass
