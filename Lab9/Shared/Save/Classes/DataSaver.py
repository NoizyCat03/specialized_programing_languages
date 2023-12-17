"""
Module defining the DataSaver class.
"""

import os
import json
import csv


class DataSaver:
    """
    DataSaver class for saving data to different file formats (txt, json, csv).
    """

    def __init__(self, **kwargs):
        """
        Constructor for the DataSaver class.

        Args:
            package_name (str): The name of the Lab package.
            filename (str): The name of the file to be saved.
        """
        self._Lab = kwargs['package_name'] if 'package_name' in kwargs else 'trash'
        self.file_name = kwargs['filename'] if 'filename' in kwargs else 'trash'
        self.__data = 'Data'

    def get_project_path(self):
        """
        Get the project path based on the current file directory.

        Returns:
            str: The project path.
        """
        script_path = os.path.dirname(os.path.abspath(__file__))
        project_path = os.path.dirname(os.path.dirname(script_path))
        project_path_1 = os.path.dirname(project_path)

        data_path = os.path.join(project_path_1, self.__data, self._Lab)

        os.makedirs(data_path, exist_ok=True)

        return data_path

    def save_txt(self, text_data):
        """
        Save text data to a text file.

        Args:
            text_data (str): The text data to be saved.
        """
        file_path = os.path.join(self.get_project_path(), self.file_name + ".txt")

        with open(file_path, 'w') as file:
            file.write(text_data)

    def save_json(self, json_data):
        """
        Save JSON data to a JSON file.

        Args:
            json_data (dict): The JSON data to be saved.
        """
        file_path = os.path.join(self.get_project_path(), self.file_name + ".json")

        with open(file_path, 'w') as file:
            json.dump(json_data, file)

    def save_csv(self, csv_data):
        """
        Save CSV data to a CSV file.

        Args:
            csv_data (list): The CSV data to be saved.
        """
        file_path = os.path.join(self.get_project_path(), self.file_name + ".csv")

        with open(file_path, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(csv_data)

# Example usage
# saver = DataSaver(package_name="Lab_1", filename="saved_data")
# text_data = "This is text to be saved in a txt file."
# json_data = {"key": "value"}
# csv_data = [["Observation 1", "Value 1"], ["Observation 2", "Value 2"]]
# saver.save_txt(text_data)
# saver.save_json(json_data)
# saver.save_csv(csv_data)
