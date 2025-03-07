# Write a program that asks the user for a filename, then attempts to open and read the file. Handle cases where the file does not exist or cannot be read.

def read_file():
    filename = input("Enter the filename: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content: ")
            print(content)
    except FileNotFoundError:
        print("Error! file not found")
    except PermissionError:
        print(f"Error: Permission denied")
    except Exception as e:
        print("Error occured")

read_file()