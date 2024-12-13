# for loop is ideal when you know the number of times you need to repeat
# a block of code, or when you're iterating through a collection 
# (like a list, string, or range)

# Looping through a list
colors = ['red', 'green', 'blue']
for color in colors:
    print(color)

print("________")

# Looping through a list
word = "Hello"
for letter in word:
    print(letter)

print("________")

# Looping with range
for i in range(3):
    print(i)

print("________")

# Start and step with range(start, stop, step)
for i in range(2, 10, 2):
    print(i)

print("________")

# Nested for loops with multiple dimensions of data
matrix = [[1, 2], [3, 4], [5, 6]]
for row in matrix:
    for item in row:
        print(item)

print("________")

# break with for loop
for i in range(5):
    if i == 3:
        break
    print(i)

print("________")

# continue with for loop
for i in range(5):
    if i == 3:
        continue
    print(i)

print("________")
# While loop continues to run as long as a given condition is True.

# Basic while loop
counter = 0
while counter < 3:
    print(counter)
    counter += 1

print("________")

total = 0
print("total: ", total)
for i in range(1, 6):
    total += i
    print("i:", i)
    print(total)

print("________")
