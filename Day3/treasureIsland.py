print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("Please either go left or right: ").lower()
if choice1 == "left":
    choice2 = input("Please either swim or wait:")

    if choice2 == "wait":
        choice3 = input("Please choose a door: red, blue or yellow: ")

        if choice3 == "red":
            print("Burned by fire. Game Over.")
        elif choice3 == "blue":
            print("Eaten by beasts. Game Over.")
        elif choice3 == "yellow":
            print("You win!")
        else:
            print("You choose a wrong door, Game Over.")

    else:
        print("You are attacked by trout. Game Over.")

else:
    print("You fell into a hole. Game Over.")