#!/usr/bin/python3
"""The command line interpreter Cli"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command processor; hbnb console"""

    intro = "Welcome to AirBnB console. Type 'help' or '?' to list commands"
    prompt = '(hbnb) '

    def do_EOF(self, line):
        "Exit"
        return True

    def do_quit(self, line):
        "Exit"
        return True

    def handle_empty_line(self, line):
        """
        Eliminates empty line execution
        """
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
