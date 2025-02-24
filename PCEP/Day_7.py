# Challenge 3: Number Categorizer
'''Write a program that asks the user to enter a number and categorizes it as:

Positive and even
Positive and odd
Negative and even
Negative and odd
Zero
'''

number = int(input("Please enter a number to check if its positive/negative and odd/even: "))


if number == 0:
   print(f"You have entered {number}")
elif number % 2 == 0 and number > 0:
   print(f"{number} is a positive even number")
elif number % 2 == 0 and number < 0:
   print(f"{number} is a negative even number")
elif number % 2 != 0 and number > 0:
   print(f"{number} is positive odd number")
elif number % 2 != 0 and number < 0:
   print(f"{number} is negative odd number")
