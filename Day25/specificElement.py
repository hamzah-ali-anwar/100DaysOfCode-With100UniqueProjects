# Write a program that searches for a specific number in a list. If the number is found, print "Found" and stop searching. If the loop completes without finding the number, print "Not Found" using the else block.

numbers = [3, 7, 1, 9, 12, 5]
target = int(input("Enter a number to search: "))

for num in numbers:
    if num == target:
        print("Found")
        break
else:
    print("Not Found")