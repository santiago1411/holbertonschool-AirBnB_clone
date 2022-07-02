#!/usr/bin/python3

"""module"""

import cmd
import models

class HBNBCommand(cmd.Cmd):
    """class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Command to exit the program
        """
        return True
    
    def do_EOF(self, arg):
        """
        Command to exit the program
        """
        return True

    def emptyline(self):
        """
        Empty line
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
