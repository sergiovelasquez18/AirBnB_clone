#!/usr/bin/python3
"""console"""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBcosole"""
    prompt = "(hbnb)"

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
