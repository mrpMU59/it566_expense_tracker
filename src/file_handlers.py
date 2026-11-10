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
        