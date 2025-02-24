# Challenge 1: Grade Calculator

''' Write a program that asks the user to input a test score (0-100) and prints the corresponding letter grade:

A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: Below 60
'''

test_score = int(input("Please enter your test score: "))

if 90 <= test_score <= 100:
    print("You have got A")
elif 80 <= test_score <= 89:
    print("You have got B")
elif 70 <= test_score <= 79:
    print("You have got C")
elif 60 <= test_score <= 69:
    print("You have got D")
else:
    print("You have failed the test")