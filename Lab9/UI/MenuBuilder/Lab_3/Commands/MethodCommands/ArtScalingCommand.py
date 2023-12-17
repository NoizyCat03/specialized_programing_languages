from Shared.Command.Command import Command
from Classes.Lab_3.art_generator import ArtGenerator


class ArtScalingCommand(Command):
    """
    Command can implement create art .
    """

    def __init__(self, executor: ArtGenerator):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.scaling()
