try:
    iterator = iter([1, 2, 3])
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    print("Error: No more items to iterate")