import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """quit console"""
        return True

    def do_EOF(self, arg):
        """
        EXit the program on OF (Ctrl + D)
        """
        return True

    def emptyline(self):
        """
        Donothing when empty line is entered
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()


