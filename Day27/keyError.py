try:
    my_dict = {"name":"Hamza", "age": 25}
    print(my_dict["city"])
except KeyError:
    print("Error: Key not found in dictionary")
