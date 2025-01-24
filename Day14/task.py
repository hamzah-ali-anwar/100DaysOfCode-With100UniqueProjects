# This section is to understant set()
# A set automatically removes duplicate elements.

''' Creating an Empty Set:

Use set() to create an empty set. (Using {} creates an empty dictionary, not a set.)
'''
empty_set = set()
print(empty_set)

'''Converting an Iterable to a Set:

Pass any iterable (e.g., list, tuple, string) to set() to create a set of unique elements.'''

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)

print("________")

# Removing Duplicates from a List:
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)

# from a string
word = "Hello"
unique_letters = set(word)
print(word)

# Membership Testing:
fruits = set(['apple', 'banana', 'mango'])
print('apple' in fruits)
print('orange' in fruits)

# Finding Common Elements Between Two Lists:
list1 = [1, 2, 3, 4, 5]
list2 = [1, 3, 5, 7, 9]
# The intersection() method in Python is used with sets to find the common elements between two or more sets.
common = set(list1).intersection(set(list2))
print(common)