# Challenge 1: Remove Duplicates
''' Write a program that removes duplicates from a list while maintaining the original order.

Create a function remove_duplicates(lst) that takes a list as input and returns a new list with duplicates
removed.
'''

def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

input_list = [1, 2, 2, 3, 4, 3, 5]
output_list = remove_duplicates(input_list)
print(output_list) 