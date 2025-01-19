# for loops are used for any iterable objects

''' Iterable is any object that you can iterate over, meaning you can access its elements
one at a time.
List, Tuples, Sets, Dictionaries, Strings and Ranges
'''
# List
numbers = [1, 2, 3]
for number in numbers:
    print(number)

print("_______")

# String
characters = "hello"
for char in characters:
    print(char)

print("_______")

# Typles
coordinates = (1, 2, 3)
for coordinate in coordinates:
    print(coordinate)

print("_______")

# Sets
unique_numbers = {1, 2, 3}
for unique_number in unique_numbers:
    print(unique_number)

print("_______")

# Dictionary
student_scores = {"Alice": 90, "Bob": 85}
# When iterating over a dictionary, using .items() allows you to unpack both the key and the value in one step.
for student_score in student_scores.items():
    print(student_score)

print("_______")

# To get the key only
student_scores = {"Alice": 90, "Bob": 85}
for key in student_scores:
    print(key)

print("_______")

# To get value only
student_scores = {"Alice": 90, "Bob": 85}
for value in student_scores.values():
    print(value)