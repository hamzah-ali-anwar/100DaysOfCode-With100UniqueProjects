# Challenge 1: Guess the Number
'''Write a program that generates a random number between 1 and 100 and asks the user 
to guess it.

The program should give feedback ("Too high" or "Too low") after each guess.
The loop continues until the user guesses the number correctly.
'''

import random

random_number = random.randint(1, 100)
user_input = int(input("Please enter a number between 1 to 100: "))

while random_number != user_input:
    if user_input < random_number:
        print("Too low")
    else:
        print("Too high")
    
    user_input = int(input("Please enter a number between 1 to 100: "))

print(f"Numbers matched {random_number}")
