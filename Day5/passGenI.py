import random

letters = ['a', 'b', 'C', 'd', 'E', 'F', 'g', 'h', 'I', 'J', 'K', 'l', 'm', 'n', 'O', 'P']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("Welcome to the PyPassword Generator!")
num_of_letters = int(input("How many letters would you like in your password? "))
num_of_numbers = int(input("How many numbers would you like in your password? "))
num_of_symbols = int(input("How many symbols would you like in your password? "))

password = ""

for char in range(1, num_of_letters + 1):
    random_char = random.choice(letters)
    password = password + random_char
    
for char in range(1, num_of_numbers + 1):
    random_char = random.choice(numbers)
    password = password + random_char

for char in range(1, num_of_symbols + 1):
    random_char = random.choice(symbols)
    password = password + random_char
    
print(password)