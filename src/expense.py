from datetime import date


class Expense:
    def __init__(self, expense_date, category, description, amount):
        self.date = expense_date
        self.category = category
        self.description = description
        self.amount = amount
