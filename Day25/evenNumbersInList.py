# Write a program that checks if a list contains any even numbers. If an even number is found, print "Even number found" and stop. If the loop completes without finding an even number, print "No even numbers" using else.

numbers = [1, 3, 4, 7, 9]

for num in numbers:
    if num % 2 == 0:
        print("Even number found")
        break
else:
    print("No even numbers")