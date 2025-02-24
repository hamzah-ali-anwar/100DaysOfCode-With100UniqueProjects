# Pizza 
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
price = 0


if size == "S":
    price = 10
    print(f"Small Pizza is {price}")
elif size == "M":
    price = 14
    print(f"Medium pizza is {price}")
elif size == "L":
    price = 16
    print(f"Large pizza is {price}")

pineapple = input("Do you want pineapple on your pizza? Y or N:")
if pineapple == "Y":
    price += 2

extra_cheese = input("Do you want extra cheese? Y or N:")
if extra_cheese == "Y":
    price += 2
    print(f"Your final bill is ${price}")

else:
    print(f"Your final bill is ${price}")