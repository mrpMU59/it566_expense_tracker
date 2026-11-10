""" Contains the list of expenses and works with it. """

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        """ Method adds an Expense object to the collection. """
        self.expenses.append(expense)

    def return_all(self):
        """ Returns all expenses sorted by date. """
        def get_date(expense):
            return expense.date
        
        return sorted(self.expenses, key=get_date) # https://docs.python.org/3/builtins/functions.html#sorted

    def replace_all(self, expenses):
        """ When opening a file, method replaces everything with a new list. """
        self.expenses = list(expenses) # https://docs.python.org/3/builtins/stdtypes.html#list

    def filter_expenses(self, start_date=None, end_date=None, category=None): # https://docs.python.org/3/builtins/constants.html#None
        """ Returns expenses matching the filters. """
        results = []

        for expense in self.return_all():
            if start_date is not None and expense.date < start_date: # https://www.geeksforgeeks.org/python/python-none-keyword/
                continue
            if end_date is not None and expense.date > end_date:
                continue
            if category and expense.category.lower() != category.lower(): # Computer Scripting Techniques with Python (1st ed.), Ch 3.2.1
                continue
            results.append(expense)

        return results

    @staticmethod # https://docs.python.org/3/builtins/functions.html#staticmethod
    def total_price(expenses):
        """ Adds up the expenses amount in a list. """
        return sum(expense.amount for expense in expenses)

    def __len__(self): # https://www.geeksforgeeks.org/python/python-__len__-magic-method/
        """ When len(manager) is written, gets the number of expenses. """
        return len(self.expenses)

    