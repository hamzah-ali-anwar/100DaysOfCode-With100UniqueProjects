# Challenge 2: Tuple Unpacking
''' Write a program that:

Creates a tuple containing the details of a person: ('John', 28, 'Engineer') (name, age, occupation).
Use tuple unpacking to extract the values into separate variables (name, age, occupation).
Print the extracted values in a formatted sentence.'''

tup = ('John', 28, 'Engineer')

name, age, occupation = tup

print(f"Name:{name}, Age:{age}, Occupation:{occupation}")

