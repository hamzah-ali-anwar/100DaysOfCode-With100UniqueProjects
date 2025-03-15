try:
    with open("file.txt", "r") as file:
        file.write("Hello") # writing in read mode, correct format "w"
except IOError:
    print("Error: Cannot write to a read-only file")