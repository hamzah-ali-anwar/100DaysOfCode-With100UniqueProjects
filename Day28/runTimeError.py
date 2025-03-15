def infinite_recursion():
    return infinite_recursion()

try:
    infinite_recursion()
except RuntimeError:
    print("Error: Maximum recursion depth exceeded.")

    