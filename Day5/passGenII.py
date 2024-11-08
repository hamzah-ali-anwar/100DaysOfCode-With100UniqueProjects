import random

letters = ['a', 'b', 'C', 'd', 'E', 'F', 'g', 'h', 'I', 'J', 'K', 'l', 'm', 'n', 'O', 'P']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("Welcome to the PyPassword Generator!")
num_of_letters = int(input("How many letters would you like in your password? "))
num_of_numbers = int(input("How many numbers would you like in your password? "))
num_of_symbols = int(input("How many symbols would you like in your password? "))

password = ""

for char in range(0, num_of_letters):
    password += random.choice(letters)
    
for char in range(0, num_of_numbers):
    password += random.choice(numbers)

for char in range(0, num_of_symbols): 
    password += random.choice(symbols)
    
print(password)