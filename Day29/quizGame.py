print("Welcome to my computer quiz game!") # simple print msg

playing = input("Do you want to play? ") # taking user's input

if playing != "yes": # if user's response is anything other then yes, then program quits
    quit()

print("Let's play :)") # will appear if user responds yes to above question

answer = input("What does CPU stands for? ") # first question

# if, else statement to verify users response 
if answer == "central processing unit":
    print("Correct")
else:
    print("Incorrect")

answer = input("What does GPU stands for? ") #  second question

# if, else statement to verify users response 
if answer == "graphics processing unit":
    print("Correct")
else:
    print("Incorrect")

answer = input("What does RAM stands for? ") # third question

# if, else statement to verify users response 
if answer == "random access memory":
    print("Correct")
else:
    print("Incorrect")

answer = input("What does PSU stands for? ") # fourth question

# if, else statement to verify users response 
if answer == "power supply":
    print("Correct")
else:
    print("Incorrect")