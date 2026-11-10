""" File contains classes that read and write to files. """

import csv
import json

from expense import Expense


class JSONFileHandler:
    """ Saves and loads a list of Expense objects as a JSON file. """

    def __init__(self, filename):
        self.filename = filename

    def save_expenses(self, expenses):
        """ Writes expenses to a JSON file. """
        data = [expense.to_dict() for expense in expenses]
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=2) # https://www.geeksforgeeks.org/python/reading-and-writing-json-to-a-file-in-python/

    def load_expenses(self):
        """ Reads the JSON file and returns a list of Expense objects. """
        """ AI was used for defining and differentiating the types of errors. """
        with open(self.filename, "r") as file:
            try:
                data = json.load(file) # https://www.geeksforgeeks.org/python/reading-and-writing-json-to-a-file-in-python/
            except json.JSONDecodeError: # https://www.geeksforgeeks.org/python/json-parsing-errors-in-python/
                raise ValueError("That file is not a valid JSON.") 

        try:
            return [Expense.from_dict(item) for item in data]
        except (KeyError, TypeError): # https://docs.python.org/3/builtins/exceptions.html#TypeError
            raise ValueError("The file has missing or incorrect expense data.")

    