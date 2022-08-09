#!/usr/bin/python3
"""The console"""


import cmd
import shlex #used for spliting
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}

class HBNBCommand(cmd.Cmd):
    """An entry point for the airbnb clone HBNB CLI"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """quits the console program"""
        return True

    def do_EOF(self, arg):
        """Exits the console"""
        return True

    def emptyline(self):
        """overite/skip the emptyline method"""
        return False
    
    def do_create(self, arg):
        """creates a new instance of BaseModel
        saves instance to a JSON file and prints the id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print(" **class name missing **")
            return False
        if args[0] in classes:
            instance = classes[args[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()
    
        
        
if __name__ == "__main__":
    HBNBCommand().cmdloop()
