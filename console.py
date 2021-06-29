#!/usr/bin/python3
""" console  """

import cmd
from models.base_model import BaseModel
from models import storage
import shlex

class HBNBCommand(cmd.Cmd):
    """ prompt of the command interpreter """
    prompt = '(hbnb)'

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
                print (new_object.id)
            except BaseException:
                print("** class doesn't exist **")

    def do_show(self, args):
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
