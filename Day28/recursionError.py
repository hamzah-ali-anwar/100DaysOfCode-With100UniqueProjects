try:
    def recurse():
        recurse()

    recurse()
except RecursionError:
    print("Error: Recursion limit reached")

