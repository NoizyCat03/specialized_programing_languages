from Shared.Command.Command import Command
from Classes.Lab_5.figure import Figure


class SetScalingCommand(Command):
    """
    Command can implement create art .
    """

    def __init__(self, executor: Figure, scaling: int):
        self.__executor = executor
        self.__scaling = scaling

    def execute(self) -> None:
        self.__executor.scaling = self.__scaling
