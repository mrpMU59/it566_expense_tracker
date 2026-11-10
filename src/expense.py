from datetime import date


class Expense:
    def __init__(self, expense_date, category, description, amount):
        self.date = expense_date
        self.category = category
        self.description = description
        self.amount = amount
        
    def to_dict(self): # Converts this expense to a dictionary for JSON and CSV, https://www.geeksforgeeks.org/python/convert-class-object-to-json-in-python/
        return {
            "date": self.date.isoformat(), # https://docs.python.org/3/library/datetime.html#datetime.date.isoformat
            "category": self.category,
            "description": self.description,
            "amount": self.amount,
        }

    @classmethod
    def from_dict(cls, data): # Creates an Expense from a dictionary
        return cls(
            date.fromisoformat(data["date"]), # https://docs.python.org/3/library/datetime.html#datetime.date.fromisoformat
            data["category"],
            data["description"],
            float(data["amount"]),
        )

    