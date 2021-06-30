#!/usr/bin/python3
""" console  """

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """ prompt of the command interpreter """
    prompt = '(hbnb) '

    def do_quit(self, _input):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, _input):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER not execute anything"""
        pass

    def do_create(self, args):
        """Creates a new instance of Case name

        Args:
            args (string):the args must be a clase name allowed in the program
        """
        if not args:
            print("** class name missing **")
        else:
            args = shlex.split(args)
            try:
                new_object = globals()[args[0]]()
                new_object.save()
                print(new_object.id)
            except BaseException:
                print("** class doesn't exist **")

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id

        Args:
            args (1) Class_Name: Name of the class to search
            args (2) id: id of the object to search
        """
        if not args:
            print("** class name missing **")
        else:
            args = shlex.split(args)
            if args[0] in globals():
                if len(args) > 1:
                    dict_show = storage.all()
                    key = args[0]+"."+args[1]
                    if key in dict_show:
                        print(dict_show[key])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id

        Args:
            args (1) Class_Name: Name of the class to destroy
            args (2) id: id of the object to destroy
        """
        if not args:
            print("** class name missing **")
        else:
            args = shlex.split(args)
            if args[0] in globals():
                if len(args) > 1:
                    obj_destroy = args[0]+"."+args[1]
                    if obj_destroy in storage.all():
                        storage.all().pop(obj_destroy)
                        storage.save()
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_all(self, args):
        """
        Prints all string representation of all instances based
        or not on the class name

        Args:
            args (1) Class Name: this arg is optional.
                show all objects that esist
                in the program of the class name.
        """
        all_list = []
        if not args:
            for instan in storage.all().values():
                all_list.append(instan.__str__())
        else:
            args = shlex.split(args)
            if args[0] in globals():
                for key, value in storage.all().items():
                    if value.__class__.__name__ == args[0]:
                        all_list.append(value.__str__())
            else:
                print("** class doesn't exist **")
                return
        print(all_list)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute

        Args:
            args (1) Class Name: [description]
            args (2) id: [description]
            args (3) attribute: [description]
            args (4) attribute value: [description]
        """
        if not args:
            print("** class name missing **")
        else:
            args = shlex.split(args)
            if args[0] not in globals():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            elif args[0]+"."+args[1] not in storage.all():
                print("** no instance found **")
            else:
                key = args[0]+"."+args[1]
                instance = storage.all()[key]
                instance.__dict__[args[2]] = args[3]
                instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
