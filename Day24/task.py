info = {"name":"Karan", "age":20, "eligible":True}

print(info) # print out the whole thing

print("________")

print(info["name"]) # prints name value

print("________")

print(info.get("name")) # prints name only but doesn't throw an error if the enetred key is wrong

print("________")

for key in info.keys():
    print(info[key])