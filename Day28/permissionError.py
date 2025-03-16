try:
    with open("file.txt", "r") as file:
        print(file.read())
except PermissionError:
    print("Error: You do not have permission to access this file")