# Create a program that checks if a year is a leap year.
leap_year = int(input("Please enter the year to see if it's a leap year: "))

if (leap_year % 4 == 0 and leap_year % 100 != 0) or (leap_year % 400 == 0):
    print(f"{leap_year} is a leap year")
else:
    print(f"{leap_year} is not a leap year")
