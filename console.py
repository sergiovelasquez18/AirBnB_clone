#!/usr/bin/python3
"""console"""

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNBcosole"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Ctrl D command to exit the program"""
        return True

    def emptyline(self):
        """command added to avoid that an empty
        line + ENTER executes anything
        """
        return cmd.Cmd.postloop(self)

    def do_create(self, args):
        if len(args) == 0:
            print("vuelvase serio mano")
        instance = BaseModel()
        print(instance.id)
        instance.save()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
