from Shared.Command.Command import Command
from Classes.Lab_7.requests_api import RequestsAPI


class BuildListCommand(Command):
    """
    Command can implement create art .
    """

    def __init__(self, executor: RequestsAPI):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.get_list()
