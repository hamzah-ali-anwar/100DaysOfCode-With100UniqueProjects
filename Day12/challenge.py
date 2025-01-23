# function using tuples as parameters

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)
    
result = average(5, 6, 7, 1)
print(result)