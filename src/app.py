""" File contains the menu and all user interactions. """

import os
from datetime import datetime

from expense import Expense
from expense_manager import ExpenseManager
from file_handlers import JSONFileHandler, CSVExporter

DEFAULT_JSON = "expenses.json"
DEFAULT_CSV = "expenses.csv"

class ExpenseTrackerApp:
    def __init__(self):
        self.manager = ExpenseManager()

    