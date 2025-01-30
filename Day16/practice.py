# Challenge 3: Tuple Indexing and Slicing
'''Write a program that:

Creates a tuple of numbers: (1, 2, 3, 4, 5, 6).
Extracts the first three elements using tuple slicing.
Extracts the last two elements using negative indexing.
Prints both results.'''

tup = (1, 2, 3, 4, 5 , 6)

tup_slicing = tup[:3]
neg_slicing = tup[-2:]

print(tup_slicing)
print(neg_slicing)