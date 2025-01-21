# Challenge 3: Collatz Sequence
''' Write a program that prompts the user to input a positive integer and then repeatedly applies 
the following rules until the number becomes 1:

If the number is even, divide it by 2.
If the number is odd, multiply it by 3 and add 1.
'''

user_input = int(input("Please enter a positive integer: "))

if user_input <= 0:
    print("Please enter a valid integer: ")
else:
    while user_input != 1:
        print(user_input, end=" -> ")
        if user_input % 2 == 0:
            user_input //= 2
        else:
           user_input = user_input * 3 + 1
    print(user_input)