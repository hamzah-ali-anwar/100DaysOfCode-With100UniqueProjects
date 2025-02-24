# Write a for loop to print the numbers 1 to 5.
for i in range(1, 6):
   print(i)

print("________")

# Write a while loop to print numbers from 10 down to 1.
x = 10
while x > 0:
    print(x)
    x -= 1

print("________")

# Write a loop that prints the square of each number in a list of numbers.
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print((number ** 2))

print("________")

# Write a loop that stops when a number greater than 50 is encountered in a list of numbers.
numbers_list = [23, 43, 22, 45, 59, 67, 32]
for num in numbers_list:
    if num > 50:
        break
    print(num)