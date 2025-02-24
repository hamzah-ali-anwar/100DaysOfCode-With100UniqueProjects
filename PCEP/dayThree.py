# For loop challenges

# prite a for loop to print numbers from 1 to 10
for num in range(1, 10):
    print(num)

# Write a program that calculates the sum of all numbers in a list using a for loop.
number = [1, 2, 3, 4, 5]
total = 0

for num in number:
    total += num
    print(total)

# Write a program to print a right-angled triangle pattern of stars (*) with 5 rows.

rows = 5
for i in range(1, rows + 1):
    print("*" * i)

# Write a program to count how many even and odd numbers are in a list using a for loop.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_count = 0
odd_count = 0

for num in my_list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even:", even_count)
print("Odd:", odd_count)