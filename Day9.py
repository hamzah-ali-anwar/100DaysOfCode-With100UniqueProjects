# Challenge 1: Multiplication Table Generator

''' Write a program that asks the user for a number and prints the multiplication table for that number 
    up to 10.
'''

number = int(input("Please enter a number: "))

for num in range(1, 11):
    result = number * num
    print(f"{number} X {num} = {result}")