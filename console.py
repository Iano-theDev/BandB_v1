#!/usr/bin/python3
"""The console"""


import cmd


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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
