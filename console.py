#!/usr/bin/python3
""" console  """

import cmd

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
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
