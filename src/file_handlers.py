""" File contains classes that read and write to files. """

import csv
import json

from expense import Expense


class JSONFileHandler:
    """ Saves and loads a list of Expense objects as a JSON file. """

    def __init__(self, filename):
        self.filename = filename

        