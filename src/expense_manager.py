""" Contains the list of expenses and works with it. """

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        """ Method adds an Expense object to the collection. """
        self.expenses.append(expense)

    