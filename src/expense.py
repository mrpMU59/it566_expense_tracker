from datetime import date


class Expense:
    def __init__(self, expense_date, category, description, amount):
        self.date = expense_date
        self.category = category
        self.description = description
        self.amount = amount

    """ Converts this expense to a dictionary for JSON and CSV. """
    def to_dict(self): # https://www.geeksforgeeks.org/python/convert-class-object-to-json-in-python/
        return {
            "date": self.date.isoformat(), # https://docs.python.org/3/library/datetime.html#datetime.date.isoformat
            "category": self.category,
            "description": self.description,
            "amount": self.amount,
        }

    """ Creates an Expense from a dictionary. """
    @classmethod
    def from_dict(cls, data):
        return cls(
            date.fromisoformat(data["date"]), # https://docs.python.org/3/library/datetime.html#datetime.date.fromisoformat
            data["category"],
            data["description"],
            float(data["amount"]),
        )

    """ Controls what print(expense) shows. """
    def __str__(self):
        return (f"{self.date.isoformat():<12}{self.category:<16}"
                f"{self.description:<20}{self.amount:>8.2f}") # https://www.geeksforgeeks.org/python/string-alignment-in-python-f-string/