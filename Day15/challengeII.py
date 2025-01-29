# Challenge 3: Counting and Extending a List
''' Write a program that:

Creates a list of colors: ["red", "blue", "green", "blue", "yellow"].
Counts how many times "blue" appears using count().
Extends the list by adding ["purple", "orange"] using extend().
Prints the updated list and the count of "blue".'''

colors = ["red", "blue", "green", "blue", "yellow"]
add_ons = ["purple", "orange"]

print(colors.count("blue"))

colors.extend(add_ons)


print(colors)