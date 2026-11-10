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

    def ask_date(self, prompt, required=False):
        """ Asks user for a date. """
        while True:
            text= input(prompt).strip()
            if text == "" and not required:
                return None
            try:
                return datetime.strptime(text, "%Y-%m-%d").date()
            except ValueError:
                print("Please use the format YYYY-MM-DD. For example, 2026-09-22.")

    def ask_amount(self):
        """ Asks user for expense amount. """
        while True:
            try:
                return float(input("Amount: "))
            except ValueError:
                print("Please enter a number. For example, 13.55.")

    def ask_filters(self):
        """ Asks user for optional filters. """
        print("Leave a filter blank to skip it (press Enter).")

        start = self.ask_date("Start date (YYYY-MM-DD): ")
        end = self.ask_date("End date (YYYY-MM-DD): ")
        category = input("Category: ").strip()
        return start, end, category
    