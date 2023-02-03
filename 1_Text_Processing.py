# Homework 1
# Crystal Ngo

import sys
import pathlib
import re
import pickle


class Person:
    ''' Person class is used to hold individual employee data'''
    def __init__(self, last, first, mi, id, phone):
        '''
        Initializes Person class object
        Args:
            all arguments must be strings
        Returns:
            N/A
        '''
        self.last = last        # Last name
        self.first = first      # First name
        self.mi = mi            # Middle initial
        self.id = id            # Employee ID
        self.phone = phone      # Phone number

    # Prints all data belonging to a single person
    def display(self):
        '''
        Prints employee data in a certain format
        Args:
            items in current object
        Returns:
            N/A
        '''
        print("Employee id: " + self.id)
        print("\t" + self.first + " " + self.mi + " " + self.last)
        print("\t" + self.phone + "\n")


def process_lines(line):
    '''
    Processes input so that it follows the correct format
    Args:
        line: a list of employee data, each item representing one employee
    Returns: dict
        employees stored using the Person class
    Example:
        >>>process_lines(["joe,doe,n,GS4938,335-354-6245"])
        >>>emp[0].display()
        >>>Employee id: GS4938
            Joe N Doe
            335-354-6245
    '''
    emp = {}                           # Holds processed employee data
    for i in range(len(line)):
        x = line[i].split(",")         # Separates values by comma
        x[0] = x[0].capitalize()       # Capitalizes last
        x[1] = x[1].capitalize()       # and first names
        if x[2]:
            x[2] = x[2].capitalize()   # Capitalizes middle initial
        else:
            x[2] = "X"                 # or sets it to "X" if non-applicable

        # Checks the format of ID and asks for correction if necessary
        id = re.search(r"[a-zA-Z]{2}\d{4}", x[3])
        while not id:
            print("ID is invalid: " + x[3])                 # Prints error
            print("ID is two letters followed by 4 digits") # message for user
            x[3] = input("Please enter a valid ID: ")       # Gets new input
            id = re.search(r"[a-zA-Z]{2}\d{4}", x[3])       # Checks new input

        # Checks the format of phone number and asks for correction if necessary
        pnum = re.search(r"(\d{3})-(\d{3})-(\d{4})", x[4])
        while not pnum:
            print("Phone " + x[4] + " is invalid")              # Prints error
            print("Enter phone number in form 123-456-7890")    # message for user
            x[4] = input("Enter phone number: ")                # Gets new input
            pnum = re.search(r"(\d{3})-(\d{3})-(\d{4})", x[4])  # Checks new input

        emp[i] = Person(x[0], x[1], x[2], x[3], x[4])   # Stores processed data
    return emp


# Starts program
if __name__ == '__main__':
    # Reads system argument
    if len(sys.argv) < 2:
        print('Please enter a filename as a system arg')
        quit()

    # Accesses data through relative path and allows program to run cross-platform
    rel_path = sys.argv[1]
    with open(pathlib.Path.cwd().joinpath(rel_path), 'r') as f:
        text_in = f.read().splitlines()     # List of strings where each string is a line from the data file

    # Puts processed lines into employee directory
    employees = process_lines(text_in[1:])  # Ignores heading line

    # Saves directory as pickle file
    pickle.dump(employees, open('employees.pickle', 'wb'))

    # Opens pickle file for reading
    employees_in = pickle.load(open('employees.pickle', 'rb'))

    # Prints employee directory
    print('\n\nEmployee list:\n')
    for emp_id in employees_in.keys():
        employees_in[emp_id].display()