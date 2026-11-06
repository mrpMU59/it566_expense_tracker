""" Exports expenses to a CSV file that Microsoft Excel can open. """

import csv # https://docs.python.org/3/library/csv.html


""" Write the expenses to a CSV file. """
def export_to_csv(expenses, filename):
    with open(filename, "w", newline="") as file: # https://docs.python.org/3/library/csv.html
        writer = csv.writer(file) # https://docs.python.org/3/library/csv.html#csv.writer

        # First row: column headings
        writer.writerow(["Date", "Category", "Description", "Amount"]) # https://docs.python.org/3/library/csv.html#csv.writer

        # One row per expense
        for expense in expenses:
            writer.writerow([expense["date"], expense["category"], expense["description"], expense["amount"]])
