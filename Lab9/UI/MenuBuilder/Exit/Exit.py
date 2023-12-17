"""
Module defining the Exit class, which represents an action to exit the program.
"""

import sys
from Shared.BuilderMenu.BuilderMenu import BuilderMenu


class Exit(BuilderMenu):
    """
    Class representing an action to exit the program.
    Inherits from BuilderMenu.
    """

    def run_menu(self):
        """
        Perform the action to exit the program.
        """
        sys.exit()
