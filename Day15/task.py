# Challenge 1: List Modification
'''Write a program that does the following using list methods:

Starts with an empty list.
Adds five different numbers using append().
Removes the second number using remove() or pop().
Inserts a new number at index 2 using insert().
Prints the final list.'''

#empty list
empty_list = []

# five different numbers using append
empty_list.append(10)
empty_list.append(20)
empty_list.append(30)
empty_list.append(40)
empty_list.append(50)

# with remove, value has to be entered
# empty_list.remove(20)

# pop works with index
empty_list.pop(2)

# inserting a new number at index 2
empty_list.insert(2, 100)

print(empty_list)

