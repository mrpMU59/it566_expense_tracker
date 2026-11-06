""" Expense tracker application. """

from datetime import datetime # https://docs.python.org/3/library/datetime.html#available-types

from store_data import store_expenses, read_expenses
from filter_data import filter_expenses
from export_data import export_to_csv

DEFAULT_FILE = "expenses.json" # Computer Scripting Techniques with Python (1st ed.), Ch 11.2.3

""" Function keeps asking for a date until a valid date or no date is given. """
def ask_for_date(prompt):
    while True:
        text = input(prompt).strip() # https://docs.python.org/3/builtins/stdtypes.html#str.strip

        if text == "": # if the input is nothing
            return ""

        try:
            datetime.strptime(text, "%Y-%m-%d") # Checks the format, https://docs.python.org/3/library/datetime.html#datetime.date.strptime
            return text

        except ValueError: # https://docs.python.org/3/builtins/exceptions.html#ValueError
            print("Please use the format YYYY-MM-DD, for example 2026-09-23.")


""" Function keeps asking for an amount of money until the user inputs a valid number. """
def ask_for_amount():
    while True:
        text = input("Amount: ")
        try:
            return float(text)

        except ValueError:
            print("Please enter a number, for example 13.50.")


""" Function asks the user for details about the new expense and adds it to the list. """
def add_expense(expenses):
    date = ""
    while date == "":
        date = ask_for_date("Date (YYYY-MM-DD): ")
    
    category = input("Category: ")
    description = input("Description of expense: ")
    amount = ask_for_amount()

    
