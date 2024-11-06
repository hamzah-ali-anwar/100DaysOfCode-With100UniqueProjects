print("Welcome to the rollercoaster")
height = int(input("What's your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster.")

age =  int(input("What's your age? "))
if age <= 12:
    bill = 5
    print("You pay $5.")
elif age <= 18:
    bill = 7
    print("You pay $7.")
else:
    bill = 12
    print("You pay $12.")

    wants_photo = input("Do you want to have a photo taken? y or n: ")

    if wants_photo == "y":
        bill += 3
        print(f"Your final bill is ${bill}.")

    else:
        print("Sorry, you can't ride the rollercoaster.")
    
    