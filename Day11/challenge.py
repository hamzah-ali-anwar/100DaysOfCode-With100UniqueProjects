# Challenge 2: Skipping Multiples of 3
''' Write a program that prints all the numbers from 1 to 20, except multiples of 3.

Use a continue statement to skip the multiples of 3.
'''

for num in range(1, 21):
    if num % 3 == 0:
        print(f"skipping the multiples of {num}")
        continue
    print(num)
    