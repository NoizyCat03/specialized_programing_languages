from Shared.Console.Input import InputValue
from Shared.Command.Command import Command


class SelectObjectWithDictCommand(Command):
    """
    Command can implement input text .
    """

    def __init__(self, executor: InputValue, dictionary: dict):
        self.__executor = executor
        self.__dictionary = dictionary

    def execute(self) -> None:
        self.__executor.select_object_with_dict(self.__dictionary)
