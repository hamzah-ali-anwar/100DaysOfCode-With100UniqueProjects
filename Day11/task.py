# Challenge 1: Prime Number Finder
''' Write a program that asks the user to input a positive integer and checks if it's a prime number.

Use a loop to check divisors from 2 to the square root of the number.
If a divisor is found, print "Not a prime number" and break out of the loop.
If no divisors are found, print "Prime number."
'''
import math

user_input = int(input("Please enter a positive integer: "))

if user_input > 1:
   is_prime = True
   for i in range(2, int(math.sqrt(user_input)) + 1):
      if user_input % i == 0:
         is_prime = False
         break
   if is_prime:
    print(f"{user_input} is a prime number.")
   else:
        print(f"{user_input} is not a prime number.")
else:
    print("A prime number must be greater than 1.")  