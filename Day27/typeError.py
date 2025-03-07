# Try adding a number and a string, then handle the exception

try:
    result = 5 + "5"
except TypeError:
    print("Error! can't add an integer and a string")