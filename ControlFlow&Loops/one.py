# Write an if statement that prints "Positive" if a number is greater than 0.

def positive_value():

    try:
        num = int(input("Please enter a number: "))
        if num > 0:
            return "Positive"
        else:
            return "Negative"
    except Exception as e:
        print("Error: please enter an integer")
        return "Invalid input"

result = positive_value()
print(result)