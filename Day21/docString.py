# docstring

'''Here's a multi line string also known as doc string'''

print(__doc__)

print("__________________________")

# Print a multi-line string using triple quotes.

multiline_strings = '''This is my string, we can treat it as such.
I guess that should do it'''

print(multiline_strings)

print("__________________________")

# Convert the boolean True into an integer.

boolean_true = True # returns 1 when converts to int
boolean_false = False # returns 0 when converts to int

convert_boolean_true_to_int = int(boolean_true)
convert_boolean_false_to_int = int(boolean_false)


print(convert_boolean_true_to_int)
print(convert_boolean_false_to_int)

print("__________________________")

# Explain the difference between is and ==

# is (identity operator): checks whether two variables reference the same object in memory

a = [1, 2, 3]
b = a
print(a is b)

# == (equality operator): compares the values of two objects to determine if they are equal

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
