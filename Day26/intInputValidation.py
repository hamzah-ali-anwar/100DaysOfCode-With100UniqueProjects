# Write a program that asks the user to enter an integer. Keep asking until they enter a valid integer. Use exception handling to catch invalid inputs.

try:
    number = int(input("Enter an integer: "))
    print(f"You entered: {number}")
except Exception as e:
    print("Invalid input: Please enter a number")
