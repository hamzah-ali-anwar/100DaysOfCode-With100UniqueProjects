# Challenge 2: Sorting and Reversing
'''Write a function sort_and_reverse(lst) that:

Takes a list of numbers as input.
Sorts the list in ascending order using sort().
Reverses the sorted list using reverse().
Returns the modified list.'''

def sort_and_reverst(lst):

    lst.sort()

    lst.reverse()

    return lst

numbers = [10, 20, 30, 40, 50]
result = sort_and_reverst(numbers)
print(result)




