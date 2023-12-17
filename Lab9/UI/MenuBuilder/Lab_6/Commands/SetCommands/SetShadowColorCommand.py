from Shared.Command.Command import Command
from Classes.Lab_5.figure import Figure


class SetShadowColorCommand(Command):
    """
    Command can implement create art .
    """

    def __init__(self, executor: Figure, shadow_color: str):
        self.__executor = executor
        self.__shadow_color = shadow_color

    def execute(self) -> None:
        self.__executor.shadow_color = self.__shadow_color
