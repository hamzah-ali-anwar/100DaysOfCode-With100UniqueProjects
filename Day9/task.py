# Challenge 2: Sum of a List
''' 
Write a program that takes a list of numbers (hardcoded or entered by the user) and 
calculates the sum of all the numbers in the list using a for loop.
'''

numbers = [3, 4, 6, 7, 10, 20]
sum = 0
for num in numbers:
    sum += num

print(f"The sum of the list numbers are {sum}")