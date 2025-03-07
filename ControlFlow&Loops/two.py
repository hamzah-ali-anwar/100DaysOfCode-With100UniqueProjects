# Write an if-else statement to check if a number is even or odd.

try:
    number = int(input("Enter an integer: "))
    if number < 0:
        print("Please enter a positive integer")
    elif number % 2 == 0:
        print("Even")
    else:
        print("Odd")
except Exception as e:
    print("Error: integer required")
