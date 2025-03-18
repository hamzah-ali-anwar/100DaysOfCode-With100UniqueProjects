user_input = input("Enter any value between 5 and 9: ")

if user_input.lower() == 'quit':
    quit()

try:
    number = int(user_input)
    if not 5 < number < 9:
        raise ValueError("Error: value should be an integer and in between 5 and 9")
    else:
     print(number)
except ValueError:
   print("Invalid input! Please enter a number between 5 and 9.")
