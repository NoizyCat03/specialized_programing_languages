"""
Module containing unit tests for the RequestsAPI class.
"""

import unittest
from prettytable import PrettyTable

from Classes.Lab_7.requests_api import RequestsAPI


class TestRequestsAPI(unittest.TestCase):
    """
    A class containing unit tests for the RequestsAPI class.
    """

    def setUp(self):
        """
        Set up the test environment by initializing the RequestsAPI object with default values.
        """
        self.site = 'https://jsonplaceholder.typicode.com/users'
        self.params = {}
        self.response = RequestsAPI(site=self.site, params=self.params)

    def test_get_table(self):
        """
        Test the get_table method to ensure it returns a PrettyTable object.
        """
        table = self.response.get_table()
        self.assertIsInstance(table, PrettyTable)


if __name__ == '__main__':
    unittest.main()
