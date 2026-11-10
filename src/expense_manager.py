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

        