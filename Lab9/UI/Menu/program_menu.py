"""
Module defining the PROGRAM_MENU dictionary, which maps menu options to corresponding MenuBuilder instances.
"""

from UI.MenuBuilder import *

# PROGRAM_MENU dictionary maps menu options to corresponding MenuBuilder instances
PROGRAM_MENU = {
    'Lab1': MenuLab1(),
    'Lab2': MenuLab2(),
    'Lab3': MenuLab3(),
    'Lab4': MenuLab4(),
    'Lab5': MenuLab5(),
    'Lab6': MenuLab6(),
    'Lab7': MenuLab7(),
    'Lab8': MenuLab8(),
    'EXIT': Exit(),
}
