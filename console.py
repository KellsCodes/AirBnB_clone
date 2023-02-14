#!/usr/bin/python3
"""The command line interpreter Cli"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command processor; hbnb console"""

    prompt = '(hbnb) '

    def do_EOF(self, line):
        "Exit"
        return True

    def do_quit(self, line):
        "Exit"
        return True

    def empty_line(self, line):
        """
        Eliminates empty line execution
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
