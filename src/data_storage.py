""" Loads expenses data and stores it in a JSON formatted file. """

import json # To store data as a JSON file


""" Function to write and store the list of expenses to a JSON file. """
def store_expenses(expenses, filename):
    with open(filename, "w") as file: # Computer Scripting Techniques with Python (1st ed.), Ch 16.1.1
        json.dump(expenses, file) # https://www.geeksforgeeks.org/python/reading-and-writing-json-to-a-file-in-python/


""" Function to read the expenses list from a JSON file.
    Returns an empty list if the file does not exist or if the file in invalid as a JSON. """
def read_expenses(filename):
    try:
        with open(filename, "r") as file: # Computer Scripting Techniques with Python (1st ed.), Ch 16.1.1
            return json.load(file) # https://www.geeksforgeeks.org/python/reading-and-writing-json-to-a-file-in-python/

    except FileNotFoundError:
        print(filename, ": not found")
        return [] # Empty list
