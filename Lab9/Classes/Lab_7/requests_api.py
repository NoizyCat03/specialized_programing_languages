"""
Module for working with HTTP requests and visualizing data using PrettyTable.
"""

import json

import requests
from prettytable import PrettyTable
from colorama import Style, Fore


class RequestsAPI:
    """
    Class for making HTTP requests and visualizing data using PrettyTable.
    """

    def __init__(self, **kwargs):
        """
        Initialize the RequestsAPI object with optional parameters.

        :param site: The URL of the site to make requests to.
        :param color: The color for styling PrettyTable headers.
        :param font: The font style for styling PrettyTable headers.
        """
        self._result = PrettyTable()
        self._site = kwargs.get('site', '')
        self._history = []
        self._headers = []
        self._color = Fore.CYAN
        self._font = Style.NORMAL
        self._reset = Style.RESET_ALL

        self._data = json

    def generate_data(self):
        """
        Generate data by making an HTTP GET request to the specified site.

        :return: The JSON data obtained from the site.
        """
        return requests.get(self._site).json()

    def get_table(self):
        """
        Create a PrettyTable from the JSON data and set the result.

        Raises:
            ValueError: If the data format is incorrect.
        """
        self._data = self.generate_data()
        table = PrettyTable()
        field_names = []
        if isinstance(self._data, list) and len(self._data) > 0 and isinstance(self._data[0], dict):
            headers = self._data[0].keys()
            for row in self._data:
                table.add_row(row.values(), divider=True)
        elif isinstance(self._data, dict):
            headers = self._data.keys()
            table.add_row(self._data.values(), divider=True)
        else:
            raise ValueError("Incorrect format")
        table.field_names = headers
        for field_name in table.field_names:
            field_names.append(self._color + self._font + field_name + self._reset)
        table.field_names = field_names
        self._result = table.get_string()

    def get_list(self):
        """
        Create a list from the JSON data and set the result.

        Raises:
            ValueError: If the data format is incorrect.
        """
        self._data = self.generate_data()
        data_list = []
        if isinstance(self._data, list) and len(self._data) > 0 and isinstance(self._data[0], dict):
            for row in self._data:
                data_list.append(list(row.values()))
        elif isinstance(self._data, dict):
            data_list.append(list(self._data.values()))
        else:
            raise ValueError("Incorrect format")

        self._result = self.list_to_str(data_list)

    @staticmethod
    def list_to_str(data_list):
        """
        Convert a list to a formatted string.

        :param data_list: The list to be converted.
        :return: The formatted string.
        """
        return '\n'.join(map(str, data_list))

    def set_style(self, header, color, font):
        """
        Set the style for PrettyTable headers.

        :param header: The header text.
        :param color: The color for styling.
        :param font: The font style for styling.
        :return: The styled header text.
        """
        return color + font + header + self._reset

    def __str__(self):
        """
        Return the string representation of the PrettyTable.

        :return: The string representation.
        """
        return self._result

    def __set_data(self):
        """
        Set the JSON data by making an HTTP GET request to the specified site.
        """
        self._data = requests.get(self._site).json()

    @property
    def history(self):
        """
        Get the request history.

        :return: The request history.
        """
        return self._history

    @property
    def font(self):
        """
        Get the font style for styling PrettyTable headers.

        :return: The font style.
        """
        return self._font

    @font.setter
    def font(self, value):
        """
        Set the font style for styling PrettyTable headers.

        :param value: The font style to set.
        """
        self._font = value

    @property
    def site(self):
        """
        Get the site URL for making requests.

        :return: The site URL.
        """
        return self._site

    @site.setter
    def site(self, value):
        """
        Set the site URL for making requests.

        :param value: The site URL to set.
        """
        self._site = value

    @property
    def color(self):
        """
        Get the color for styling PrettyTable headers.

        :return: The color.
        """
        return self._color

    @color.setter
    def color(self, value):
        """
        Set the color for styling PrettyTable headers.

        :param value: The color to set.
        """
        self._color = value


# Example usage:
# site = 'https://jsonplaceholder.typicode.com/users'
# response = RequestsAPI(site=site)
# response.get_list()
# response.get_table()
# print(response)
