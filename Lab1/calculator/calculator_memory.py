import json
import logging


# Represents calculator memory
class CalculationMemory:

    # Constructor
    def __init__(self, file_name):
        logging.info("Initializing calculator memory")
        self.__file_name = file_name
        self.__data = self.__load_data()

    # Adds record to memory
    def add_record(self, first_number, second_number, operator, result):
        logging.info('Adding record to memory')
        index = len(self.__data)
        record = {
            "index": index,
            "firstNumber": first_number,
            "secondNumber": second_number,
            "operator": operator,
            "result": result
        }
        self.__data.append(record)
        self.__save_data()

    # Gets all records
    def get_all_records(self):
        logging.info('Getting all memory records')
        return self.__data

    # Clears memory
    def clear_memory(self):
        logging.info('Clearing memory')
        self.__data = []
        self.__save_data()

    # Gets record by index
    def get_record_by_index(self, index):
        logging.info(f'Getting record #{index}')
        for record in self.__data:
            if record["index"] == index:
                return record
        return None

    # Gets formatted record
    def get_formatted_string_data(self) -> str:
        logging.info('Getting formatted memory record string')
        memory_message = ''
        for record in self.__data:
            memory_message += ("{0}) {1} {2} {3} = {4}\n"
                               .format(record['index'], record['firstNumber'], record['operator'],
                                       record['secondNumber'], record['result']))
        return memory_message

    # Loads data from file
    def __load_data(self):
        logging.info('Loading data from file')
        try:
            with open(self.__file_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    # Saves data in file
    def __save_data(self):
        logging.info('Saving data in file')
        with open(self.__file_name, 'w') as file:
            json.dump(self.__data, file)
