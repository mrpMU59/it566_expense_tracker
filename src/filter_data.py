""" Filters a list of expenses by date range and/or by category. """


""" Function to only return the expenses that match.
    If the dates or category is empty, it is ignored. """
def filter_expenses(expenses, start_date, end_date, category):
    results = []

    for expense in expenses:
        # Will skip this expense if it is before the start date
        if start_date != "" and expense["date"] < start_date: # if the start date is not empty and the expense date is less than the start date
            continue

        # Will skip this expense if it is after the end date
        if end_date != "" and expense["date"] > end_date: # if the end date is not empty and the expense date is greater than the end date
            continue

        # Will skip this expense if the category does not match
        # if the category is not empty and the expense category (lowercased) does not match
        if category != "" and expense["category"].lower() != category.lower(): # Computer Scripting Techniques with Python (1st ed.), Ch 3.2.1
            continue

        results.append(expense)

    return results


