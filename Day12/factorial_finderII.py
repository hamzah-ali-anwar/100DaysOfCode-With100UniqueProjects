# Challenge 2: Factorial Finder
''' Write a function called factorial that takes a non-negative integer as input and returns 
its factorial. Use a for loop or recursion to calculate the factorial.
'''

def factorial(num):
    if num == 0 and num == 1:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

print(factorial(5))