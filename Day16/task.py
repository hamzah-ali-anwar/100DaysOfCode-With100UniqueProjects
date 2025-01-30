# Challenge 1: Swapping Tuple Elements
''' Write a function swap_elements(tup) that:

Takes a tuple with exactly two elements.
Swaps the two elements and returns a new tuple.'''

def swap_elements(tup):
    if len(tup) == 2:
        return (tup[1], tup[0])
    else:
        print("Input tuple must have exactly two elements")

result = swap_elements((5, 10))
print(result)