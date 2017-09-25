"""
Usage:
    Dojo create_room <room_type> <room_name>...
    Dojo add_person <first_name> <second_name> <FELLOW|STAFF> [<wants_accommodation>]
    Dojo print_room <room_name>
    Dojo load_people <filename>
    Dojo print_allocations [<-o=filename>]
    Dojo print_unallocated [<-o=filename>]
    Dojo reallocate_person <first_name> <second_name> <new_room_name>
Options:
  help     Show this screen.
  clear    Clears the screen
  quit     exits the application
"""

import cmd
import os

from docopt import DocoptExit, docopt
from termcolor import cprint
from pyfiglet import Figlet, DEFAULT_FONT
from app.controller import Dojo


def intro():
    print(__doc__)


def docopt_cmd(func):
    """
    This decorator simplifies the try/except block and returns
    the result of parsing docopt using an action

    credits: https://github.com/docopt/docopt/blob/master/examples/interactive_example.py
    Contributors: JonLundy, TheWaWaR
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as err:
            # The DocoptExit is thrown when the args do not match
            # We print a message to the user and the usage block
            print('Invalid Command!')
            print(err)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn
