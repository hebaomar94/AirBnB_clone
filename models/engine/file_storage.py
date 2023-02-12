#!/usr/bin/python3
""" FileStorage Module """


import json
from models.base_model import BaseModel


class FileStorage:
    """ FileStorage class
    Attributes:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all objects
            by <class name>.id (ex: to store a BaseModel object
            with id=12121212, the key will be BaseModel.12121212)
    Methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with
                        key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects (only if the JSON
            file (__file_path) exists ; otherwise, do nothing.
            If the file doesn't exist, no exception should be raised)
    """
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """serializes instances to a JSON file
        and deserializes JSON file to instances"""

    # @objects.getter
    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    # @objects.setter
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.all().items()},
                      f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        classes = {
            'BaseModel': BaseModel
        }
        try:
            with open(FileStorage.__file_path, 'r') as f:
                js_dic = json.load(f)
                for dic in js_dic.values():
                    cls = classes[dic['__class__']]
                    obj = cls(**dic)
                    self.new(obj)
        except Exception:
            pass
