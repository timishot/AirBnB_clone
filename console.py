#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """
        EXit the program on OF (Ctrl + D)
        """
        print("")
        return True

    def emptyline(self):
        """
        Do nothing when empty line is entered
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()


