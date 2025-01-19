# Challenge 2: Sum of a List
''' 
Write a program that takes a list of numbers (hardcoded or entered by the user) and 
calculates the sum of all the numbers in the list using a for loop.
'''

user_input = input("Please enter numbers with spaces between them: ")
numbers = list(map(int, user_input.split()))

sum = 0
for num in numbers:
    sum += num
print(sum)


