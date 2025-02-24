# Challenge 2: Leap Year Checker

'''Write a program that asks the user for a year and determines if it is a leap year.

A year is a leap year if it is divisible by 4.
However, it is not a leap year if it is divisible by 100 unless it is also divisible by 400.
'''

year = int(input("Please enter a year to determine if its a leap year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} not a leap year")