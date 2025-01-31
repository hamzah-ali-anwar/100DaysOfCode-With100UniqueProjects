'''Create a program capable of displaying questions to the user like KBC. 
Use list data type to store the questions and their correct answers.
Display the final amount the person is taking home after playing the game. '''

import sys

questions = [
    {
        "question": "Which of the following is the correct way to define a function in Python?",
        "options": ["def myFunction:", "def myFunction():", "function myFunction():", "def myFunction;"],
        "answer": "def myFunction():"
    },
    {
        "question": "What will be the output of print(2 ** 3)?",
        "options": ["5", "6", "8", "9"],
        "answer": "8"
    },
    {
        "question": "Which of the following is NOT a valid variable name in Python?",
        "options": ["my_var:", "2ndValue:", "_privateVar:", "myVar123;"],
        "answer": "def myFunction():"
    },
    {
        "question": "What is the output of print(type(10 / 2))?",
        "options": ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'bool'>"],
        "answer": "8"
    }
]



print("Welcome to Prepare for PCEP Game Show!")

initial_selection = input("Please type 'y' if you wish to continue and 'n' if you wish to exit: ")

while initial_selection not in ('y', 'n'):
    print("Wrong selection, please enter y or n")
    initial_selection = input("Please type 'y' if you wish to continue and 'n' if you wish to exit: ")

if initial_selection == 'y':
    print("Welcome to Prepare for PCEP Game Show!")
else:
    print("Exiting!")
    sys.exit()


