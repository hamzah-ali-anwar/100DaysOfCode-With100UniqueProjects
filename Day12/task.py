# Challenge 1: Calculator Function
''' Write a function called calculator that takes three arguments: two numbers and an operator 
(+, -, *, /). The function should return the result of the operation.

Include error handling for invalid operators and division by zero.
'''

def calculator(num1, num2, operator):
    try:
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 == 0:
                return "Error! can't divide a number by zero"
            return num1 / num2
        else:
            raise ValueError("Invalid operator, please user +, -, *, and / operators")
    
    except Exception as e:
        return f"an unexpected error occured {e}"