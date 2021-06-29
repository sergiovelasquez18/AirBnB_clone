#!/usr/bin/python3
"""console"""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBcosole"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Ayuda del comando1"""
        print("Hasta pronto")
        return True

    def do_EOF(self, args):
        """Ayuda del comando1"""
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
