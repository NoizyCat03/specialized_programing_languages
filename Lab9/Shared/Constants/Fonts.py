"""
Module defining font-related dictionaries using colorama.
"""

from colorama import Style

# Dictionary for font styles
FONTS = {
    'NORMAL': Style.NORMAL,
    'BRIGHT': Style.BRIGHT,
    'DIM': Style.DIM,
}

# Example usage:
# print(f"{FONTS['BRIGHT']}This text is in a bright font style.{Style.RESET_ALL}")
