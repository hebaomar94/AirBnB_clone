#!/usr/bin/python3
""" BaseModel Module """


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ BaseModel class
    Atrributes:
            id: unique id for each BaseModel
            created_at: datetime - assign with the current datetime
            updated_at: datetime - update the current datetime
    Methods:
            save(self): updates the public instance attribute 'updated_at'
                        with the current datetime
            to_dict(self): returns a dictionary containing all keys/values
                        of __dict__ of the instance
    """

    def __init__(self, *args, **kwargs):
        """defines all common attributes/methods for other classes
        """
        if kwargs:
            for key in kwargs:
                if key == '__class__':
                    continue
                if key in ('created_at', 'updated_at'):
                    self.__setattr__(key, datetime.fromisoformat(kwargs[key]))
                else:
                    self.__setattr__(key, kwargs[key])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dict = {'__class__': self.__class__.__name__}
        dict.update(self.__dict__)
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()
        return dict
