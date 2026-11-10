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

    def ask_filename(self, prompt, default):
        """ Asks user for a file name. """
        name = input(f"{prompt} (press Enter for {default}): ").strip()
        return name if name else default

    
    def show_menu(self):
        print()
        print("===== Expense Tracker =====")
        print("1. Add an expense")
        print("2. View expenses (with optional filters)")
        print("3. Open an expense file")
        print("4. Save expenses to a file")
        print("5. Export expenses to CSV (for Excel)")
        print("6. Quit")

    def add_expense(self):
        expense_date = self.ask_date("Date (YYYY-MM-DD): ", required=True)
        category = input("Category: ").strip()
        description = input("Description: ").strip()
        amount = self.ask_amount()

        expense = Expense(expense_date, category, description, amount)

        self.manager.add_expense(expense)

        print("Expense added!")

    def view_expenses(self):
        start, end, category = self.ask_filters()
        matches = self.manager.filter(start, end, category)
        self.print_expenses(matches)

    def print_expenses(self, expenses):
        if not expenses:
            print("No expenses to show.")
            return
        print()
        print("Date         Category        Description         Amount")
        print("-" * 60)
        for expense in expenses:
            print(expense)
        print("-" * 60)
        print(f"Total: {self.manager.total(expenses):.2f}")

    def open_file(self):
        filename = self.ask_filename("File to open", DEFAULT_JSON)
        try:
            expenses = JSONFileHandler(filename).load()
        except FileNotFoundError:
            print("File not found: ", filename)
            return
        except ValueError as error:
            print("Could not open file: ", error)
            return

        self.manager.replace_all(expenses)
        print(f"Loaded {len(self.manager)} expenses.")

    def save_file(self):
        filename = self.ask_filename("Save as", DEFAULT_JSON)
        try: 
            JSONFileHandler(filename).save(self.manager.return_all())
            print(f"Saved {len(self.manager)} expenses to {os.path.abspath(filename)}") # https://docs.python.org/3/library/os.path.html#os.path.abspath
        except OSError as error:
            print("Could not save file: ", error)

    def export_csv(self):
        filename = self.ask_filename("CSV file name", DEFAULT_CSV)
        start, end, category = self.ask_filters()
        matches = self.manager.filter(start, end, category)

        try:
            CSVExporter(filename).export(matches)
            print(f"Exported {len(matches)} expenses to {os.path.abspath(filename)}") # https://docs.python.org/3/library/os.path.html#os.path.abspath
        except OSError as error:
            print("Could not export: ", error)


    def run_app(self):
        actions = {"1": self.add_expense, "2": self.view_expenses, "3": self.open_file,
                   "4": self.save_file, "5": self.export_csv}

        while True:
            self.show_menu()
            choice = input("Choose an option (1-6): ").strip()

            if choice == "6":
                print("Goodbye!")
                break
            elif choice in actions:
                actions[choice]()
            else:
                print("Invalid choice. Please type a number from 1 to 6.")