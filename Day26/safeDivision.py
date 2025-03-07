# Write a program that takes two numbers as input and performs division. Handle cases where the user enters non-numeric values and when division by zero occurs.

try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print(f"The division of two variables is: {result}")

except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")