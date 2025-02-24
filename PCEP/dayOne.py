'''
    Program that takes two integers and perform calculations
'''
firstValue = int(input("Please enter first value: "))
secondValue = int(input("Please enter second value: "))

calc = int(input("Please choose the calculation you'd like to perform: \n 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division \n 5 for floorDivision \n 6 for modulus \n 7 for exponentiation\n :"))

if calc == 1:
    print(f"Sum of these values: {firstValue + secondValue}")  #  Addition
elif calc == 2:
    print(f"Difference of these values: {firstValue - secondValue}") # Subtraction
elif calc == 3:
    print(f"Muliplication result: {firstValue * secondValue}") # Multiplication
elif calc == 4:
    print(f"Division result: {firstValue / secondValue}") # Division
elif calc == 5:
    print(f"Rounded value: {firstValue // secondValue}") # Floor Division
elif calc == 6:
    print(f"Remainder: {firstValue % secondValue}") # Modulus/Remainder
elif calc == 7:
    print(f"Exponentiation: {firstValue ** secondValue}") # Exponentiation
else:
    print("Please enter a valid number")