#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import  State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review



class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    model_classes = {
            "BaseModel": BaseModel,
            "User" : User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def do_create(self, line):
        """ create a instance """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.model_classes:
            print("** class doesn't exists **")
            return

        new_instance = self.model_classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """ show me the value of instance """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.model_classes:
            print("** class doesn't exists **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            instance_id = args[1]

        key = "{}.{}".format(class_name, instance_id)

        if key not in storage.all().keys():
            print("** no instance found **")
            return

        instance = storage.all()[key]
        print(instance)

    def do_destroy(self, line):
        """ Destroy a instance"""
        args = line.split()

        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.model_classes:
            print("** class doesn't exists **")
            return

        if len(args) < 2:
            print("** instance id missing **")

        instance_id = args[1]

        key = "{}.{}".format(class_name, instance_id)

        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()
    
    def do_all(self, line):
        #show all the object stored in the storage
        args = line.split()
        
        if len(args) == 0:
            objects = storage.all().values()
            print([str(obj) for obj in objects])
        elif args[0] not in self.model_classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            if hasattr(self.model_classes[class_name], 'all'):
                instances = self.model_classes[class_name].all()
                print(instances)
            
            else:
                class_name = args[0]
                objects = [obj for obj in storage.all().values()
                        if obj.__class__.__name__ == class_name]
                print([str(obj) for obj in objects])
    def default(self, line):
        args = line.split(".")
        if len(args) == 0:
            return
        class_name =args[0]
        if class_name not in self.model_classes:
            print(" class doesn't exists **")
            return
        if len(args) == 2:
            if args[1] == "all()":
                objects = [obj for obj in storage.all().values()
                          if obj.__class__.__name__ == class_name]
                print([str(obj) for obj in objects])
            elif args[1] == "count":
                count = len(self.model_classes[class_name].all())
                print(count)
        else:
            pass

    def do_update(self, line):
        """update the storage"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing")
            return
        class_name = args[0]
        if class_name not in self.model_classes:
            print("** class doesn't exists **")
            return

        if len(args) == 1:
            print("** instance id missing")
            return

        instance_id = args[1]
        if len(args) == 2:
            print("** attribute name missing **")
            return

        key = "{}.{}".format(class_name, instance_id)

        if len(args) == 3:
            print("** value missing **")
            return
        instance = storage.all()[key]
        attribute = args[2]
        value = args[3]

        setattr(instance, attribute, value)
        instance.save()

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
