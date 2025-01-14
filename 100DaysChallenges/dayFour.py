# Strings are immutable
# upper, lower, rstrip, replace, split, capitalize, center, count, endwith, find, isalnum, isalpha, islower,
# isprintable, isspace, istitle, startswith, swapcase, title
a = "anwar !!!harry!! !!!!!!!!! harry      "
b = "12shaka"

print(a.upper())

print(a.lower())

print(a.rstrip("!"))

print(a.replace("harry", "hamza"))

print(a.split("!"))

print(a.capitalize())

print(a.center(50, "-"))

print(a.count("!"))

print(a.endswith("harry"))

print(a.find("harry"))

print(a.isalnum())

print(b.isalnum())