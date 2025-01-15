# Strings are immutable
# upper, lower, rstrip, replace, split, capitalize, center, count, endwith, find, isalnum, isalpha, islower,
# isprintable, isspace, istitle, startswith, swapcase, title

a = "anwar !!!harry!! !!!!!!!!! harry      "
b = "12shaka"
c = "  "
d = "Hello"

# Converts all characters in a string to uppercase.
print(a.upper())

# Converts all characters in a string to lowercase.
print(a.lower())

# Removes trailing characters (spaces or specified characters) from the right end of the string.
print(a.rstrip("!"))

# Replaces occurrences of a substring with another substring.
print(a.replace("harry", "hamza"))

# Splits a string into a list based on a delimiter.
print(a.split("!"))

# Converts the first character of the string to uppercase and the rest to lowercase.
print(a.capitalize())

# Centers the string within a specified width, padding it with spaces (or another character).
print(a.center(50, "-"))

# Counts the number of occurrences of a substring.
print(a.count("!"))

# Checks if a string ends with a specified suffix.
print(a.endswith("harry"))

# Finds the first occurrence of a substring and returns its index. Returns -1 if not found.
print(a.find("harry"))

# Checks if all characters in the string are alphanumeric (letters or digits).
print(a.isalnum())
print(b.isalnum())

# Checks if all characters in the string are alphabetic (letters only).
print(a.isalpha())

# Checks if all characters in the string are lowercase.
print(a.islower())

# Checks if all characters in the string are printable (e.g., no control characters like \n or \t).
print(a.isprintable())

# Checks if the string contains only whitespace characters (spaces, tabs, or newlines).
print(a.isspace())
print(c.isspace())

# Checks if the string is title-cased (i.e., the first character of each word is uppercase, and the rest are lowercase).
print(d.istitle())

# Checks if the string starts with a specified prefix.
print(a.startswith("Hello"))

# Swaps the case of all characters in the string (uppercase becomes lowercase and vice versa).
print(a.swapcase())

# Converts the string to title case (each word starts with an uppercase letter, and the rest are lowercase).
print(a.title())