# Write a program that checks if a given number is prime using a for loop. Use else with the loop to print "Prime" if no factors are found and "Not Prime" otherwise.

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break

    else:
        print("Prime")
else:
    print("Not Prime")