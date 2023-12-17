"""
Module defining color-related dictionaries using colorama.
"""

from colorama import Fore, Back, Style

# Dictionary for text colors
COLORS = {
    'BLACK': Fore.BLACK,
    'RED': Fore.RED,
    'GREEN': Fore.GREEN,
    'YELLOW': Fore.YELLOW,
    'BLUE': Fore.BLUE,
    'MAGENTA': Fore.MAGENTA,
    'CYAN': Fore.CYAN,
    'WHITE': Fore.WHITE,
    'RESET': Style.RESET_ALL,
}

# Dictionary for background colors
BACKGROUND_COLORS = {
    'BLACK': Back.BLACK,
    'RED': Back.RED,
    'GREEN': Back.GREEN,
    'YELLOW': Back.YELLOW,
    'BLUE': Back.BLUE,
    'MAGENTA': Back.MAGENTA,
    'CYAN': Back.CYAN,
    'WHITE': Back.WHITE,
}

# Example usage:
# print(f"{COLORS['RED']}This text is red.{COLORS['RESET']}")
# print(f"{BACKGROUND_COLORS['BLUE']}This text has a blue background.{STYLE.RESET_ALL}")
