print("Welcome to my computer quiz game!") # simple print msg

playing = input("Do you want to play? ") # taking user's input

if playing.lower() != "yes": # if user's response is anything other then yes, then program quits
    quit()

print("Let's play :)") # will appear if user responds yes to above question

score = 0

answer = input("What does CPU stands for? ") # first question

# if, else statement to verify users response 
correct_answer = "central processing unit"
if answer.lower() == correct_answer:
    print("Correct")
    score += 1
else:
    print(f"Wrong! correct answer is {correct_answer}")

answer = input("What does GPU stands for? ") #  second question

# if, else statement to verify users response 
correct_answer = "graphics processing unit"

if answer.lower() == correct_answer:
    print("Correct")
    score += 1
else:
    print(f"Wrong! correct answer is {correct_answer}")

answer = input("What does RAM stands for? ") # third question

# if, else statement to verify users response 
correct_answer = "random access memory"
if answer.lower() == correct_answer:
    print("Correct")
    score += 1
else:
    print(f"Wrong! correct answer is {correct_answer}")

answer = input("What does PSU stands for? ") # fourth question

# if, else statement to verify users response 
correct_answer = "power supply"
if answer.lower() == correct_answer:
    print("Correct")
    score += 1
else:
    print(f"Wrong! correct answer is {correct_answer}")

print(f"You got {score} questions correct")
print(f"You scored {round((score / 4) * 100)}%")
