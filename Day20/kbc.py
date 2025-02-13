'''Create a program capable of displaying questions to the user like KBC. 
Use list data type to store the questions and their correct answers.
Display the final amount the person is taking home after playing the game. '''

import sys
import random

questions = [
    {"question": "Which of the following is incorrect for a dictionary in Python?", 
     "options": ["Each key must be unique", "The key should be an immutable object", "The len() function returns the sum of key-value elements in the dictionary", "The len() function returns the number of key-value elements in the dictionary"], 
     "answer": "The len() function returns the sum of key-value elements in the dictionary"},

    {"question": "Python's name is derived from which of the following?", 
     "options": ["Python Café", "Python Forest", "Python snake", "Monty Python’s Flying Circus"], 
     "answer": "Monty Python’s Flying Circus"},

    {"question": "What does the method items() return in a Python dictionary?", 
     "options": ["A list of keys", "A list of values", "A list of tuples containing key-value pairs", "A list of dictionaries"], 
     "answer": "A list of tuples containing key-value pairs"},

    {"question": "A complete set of commands in Python is known as:",
     "options": ["Instruction list", "Code laws", "Command-line", "Command list"],
     "answer": "Instruction list"},

    {"question": "Which of the following statements are correct?", 
     "options": ["True + 1 evaluates to 2", "True and False evaluates to False", "True or False evaluates to False", "7 + False evaluates to False"],
     "answer": "True + 1 evaluates to 2"},

    {"question": "The octal number system has which base?", 
     "options": ["2", "8", "10", "16"], 
     "answer": "8"},

    {"question": "If a list is passed into a function’s argument and modified inside the function, what happens?", 
     "options": ["It will affect the original list", "It will not affect the original list", "It will give an error", "It will become global by default"], 
     "answer": "It will affect the original list"},

    {"question": "An integer number preceded by 0x (zero-x) is treated as:", 
     "options": ["Octal", "Binary", "Hexadecimal", "Decimal"], 
     "answer": "Hexadecimal"},

    {"question": "Who created Python?", 
     "options": ["Guido ban Rossum", "Guido van Rossum", "Guido the Russian", "Guodo van Rossum"], 
     "answer": "Guido van Rossum"},

    {"question": "The meaning of a positional parameter is determined by:", 
     "options": ["Position", "Name", "Style", "None of the above"], 
     "answer": "Position"},

    {"question": "What is the output of print(0.1 + 0.2)?", 
     "options": ["0.3", "0.30000000000000004", "0.1", "None of the above"], 
     "answer": "0.30000000000000004"},

    {"question": "If a = {5, 6, 7}, what happens when a.add(5) is executed?", 
     "options": ["a becomes {5, 6, 7}", "a becomes {5, 5, 6, 7}", "a becomes {6, 7}", "An error is raised"], 
     "answer": "a becomes {5, 6, 7}"},

    {"question": "Which of the following is a mutable data type in Python?", 
     "options": ["Tuple", "String", "List", "Integer"], 
     "answer": "List"},

    {"question": "What is the output of print(type({}))?", 
     "options": ["<class 'list'>", "<class 'dict'>", "<class 'set'>", "<class 'tuple'>"], 
     "answer": "<class 'dict'>"},

    {"question": "Which keyword is used to handle exceptions in Python?", 
     "options": ["try", "catch", "handle", "except"], 
     "answer": "except"},

    {"question": "What will be the output of the following code?\n\ndef func(x=[]):\n    x.append(1)\n    print(x)\n\nfunc()\nfunc()", 
     "options": ["[1]\n[1]", "[1]\n[1, 1]", "[1]\n[1, 1, 1]", "An error is raised"], 
     "answer": "[1]\n[1, 1]"},

    {"question": "Which of the following is the correct way to define a function in Python?", 
     "options": ["def myFunction:", "def myFunction():", "function myFunction():", "def myFunction;"], 
     "answer": "def myFunction():"},

    {"question": "What is the output of the following code?\n\nprint('Hello, World!'[7:])", 
     "options": ["Hello", "World!", "Hello, World", "Error"], 
     "answer": "World!"},

    {"question": "Which of the following is not a valid Python data type?", 
     "options": ["List", "Dictionary", "Tuple", "Array"], 
     "answer": "Array"},

    {"question": "What is the result of the expression 3 * 1**3?", 
     "options": ["27", "9", "3", "1"], 
     "answer": "3"}
]

# Prize money for each question
prize_money = [1000, 2000, 3000]  # Extend this list as needed

def play_game():
    total_won = 0
    random.shuffle(questions)  # Shuffle questions for randomness

    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for idx, option in enumerate(q['options']):
            print(f"{idx + 1}. {option}")

        try:
            answer = int(input("Enter the option number (1-4) or 0 to quit: "))
            if answer == 0:
                print(f"You chose to quit. Total money won: ${total_won}")
                sys.exit()
            elif q['options'][answer - 1] == q['answer']:
                total_won += prize_money[i]
                print(f"Correct! You've won ${prize_money[i]}. Total: ${total_won}")
            else:
                print(f"Wrong answer. The correct answer was: {q['answer']}")
                print(f"Total money won: ${total_won}")
                sys.exit()
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 4, or 0 to quit.")
            sys.exit()

    print(f"Congratulations! You've answered all questions correctly. Total money won: ${total_won}")

if __name__ == "__main__":
    print("Welcome to the KBC Game!")
    play_game()

