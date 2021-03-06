#!/usr/bin/python3

"""
class BaseModel that defines all common
methods for other classes
"""
import json


class FileStorage:
    """[class FileStorage]

    Returns:
        [data]: [serializes instances to a JSON file
        and deserializes JSON file to instances]
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Public instance

        Returns:
            [self]: [the dictionary objects]
        """
        return self.__objects

    def new(self, obj):
        """[sets in __objects the obj with key <obj class name>.id]

        Args:
            obj ([objects]): [new objets]
        """
        key_compoust = obj.__class__.__name__+"."+obj.id
        # en los diccionarios si la clave no existe la crea,
        # y si existe la reemplaza.
        self.__objects[key_compoust] = obj

    def save(self):
        """[serializes __objects to the JSON file]
        """
        dict_string = {}
        for key, value in self.__objects.items():
            dict_string[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='UTF8') as file:
            json.dump(dict_string, file, indent=4)

    def reload(self):
        """[deserializes the JSON file to __objects]
        """
        from models.base_model import BaseModel
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.user import User

        dict_desco = {}
        try:
            with open(FileStorage.__file_path) as file:
                dict_desco = json.load(file)
            for key, value in dict_desco.items():
                obj = value["__class__"]
                self.__objects[key] = locals()[obj](**value)
        except BaseException:
            pass
