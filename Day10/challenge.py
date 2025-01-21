# Challenge 2: Password Validator
''' Write a program that repeatedly asks the user to enter a password until they provide the correct one.

Hardcode the password (e.g., password = "python123").
Give feedback if the password is incorrect and exit the loop when the correct password is entered.

'''

password = "python123"
user_input = input("Guess the password: ")


while password != user_input:
    print("Incorrect")

    user_input = input("Guess the password: ")

print("Password matched")