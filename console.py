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
        ''' Creates a new instance of clase name'''
        if not args:
            print("** class name missing **")
        else:
            args = shlex.split(args)
            try:
                new_object = globals()[args[0]]()
                new_object.save()
                print (new_object.id)
            except:
                print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
