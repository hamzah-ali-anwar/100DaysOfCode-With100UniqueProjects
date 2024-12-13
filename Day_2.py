# Tip Clculator

print('Welcome to the tip calculator!')

totalBill = float(input('What was the total bill? $'))
tip = int(input('How much tip would you like to add? 10, 12, or 15?'))
numberOfPeople = int(input('How many people to split the bill? '))

tipAmount = totalBill * tip / 100
totalAmount = totalBill + tipAmount
billPerPerson = totalAmount / numberOfPeople
totalEach = round(billPerPerson, 2)

print(f'Each person should pay ${totalEach}')