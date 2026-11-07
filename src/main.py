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

    expense = { # Computer Scripting Techniques with Python (1st ed.), Ch 15.1.2
        "date": date,
        "category": category,
        "description": description,
        "amount": amount,
    }

    expenses.append(expense)
    print("Expense added!")


""" Function prints a list of expenses and the total. """
def print_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses to show.")
        return

    print()
    print("Date         Category            Description         Amount")
    print("-" * 60)

    total = 0
    for expense in expenses:
        print(f"{expense['date']:<12}{expense['category']:<16}"
              f"{expense['description']:<20}{expense['amount']:>8.2f}") # https://www.geeksforgeeks.org/python/string-alignment-in-python-f-string/
        total = total + expense["amount"]

    print("-" * 60)
    print(f"Total: {total:.2f}")


""" Function asks the user for filter options and returns them. """
def ask_for_filters():
    print("Leave a filter blank to skip it.")
    start = ask_for_date("Start date (YYYY-MM-DD): ")
    end = ask_for_date("End date (YYYY-MM-DD): ")
    category = input("Category: ").strip() # https://docs.python.org/3/builtins/stdtypes.html#str.strip
    return start, end, category


""" Function shows the menu. """
def show_menu():
    print()
    print("===== Expense Tracker =====")
    print("1. Add an expense")
    print("2. View expenses (with optional filters)")
    print("3. Open an expense file")
    print("4. Save expenses to a file")
    print("5. Export expenses to CSV (for Excel)")
    print("6. Quit")


def main():
    expenses = [] # list that holds all the expenses

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ")

        if choice == "1": # Add an expense
            add_expense(expenses)

        elif choice == "2": # View expenses (with optional filters)
            start, end, category = ask_for_filters()
            matches = filter_expenses(expenses, start, end, category)
            print_expenses(matches)

        elif choice == "3": # Open an expense file
            filename = input("File to open (press Enter for expenses.json): ")
            if filename == "":
                filename = DEFAULT_FILE
            expenses = read_expenses(filename)
            print("Loaded", len(expenses), "expenses.")

        elif choice == "4": # Save expenses to a file
            if filename == "":
                filename = DEFAULT_FILE

            store_expenses(expenses, filename)
            print("Saved", len(expenses), "expenses.")

        elif choice == "5": # Export expenses to CSV
            filename = input("CSV file name (press Enter for expenses.csv): ")
            if filename == "":
                filename = "expenses.csv"

            start, end, category = ask_for_filters()
            matches = filter_expenses(expenses, start, end, category)
            export_to_csv(matches, filename)
            print("Exported", len(matches), "expenses to", filename)

        elif choice == "6": # Quit
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please type a number from 1 to 6.")


if __name__ == "__main__":
    main()