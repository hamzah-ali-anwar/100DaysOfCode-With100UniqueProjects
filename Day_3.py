# Treasure Island
print("Welcome to Treasure Island.")
print("Your missing is to find the treasure.")

activity = ""
door = ""

direction = input("Select L to go left and R to go right: ")
if direction == "L":
    activity = input("swim or wait: ")
if activity == "wait":
    door = input("Select R for red, B for blue and Y for yellow door: ")
if door == "Y":
    print("You won!")
else:
    print("Game Over")
