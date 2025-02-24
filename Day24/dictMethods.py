manager_one = {122: 45, 123: 89, 567: 69, 670: 69}
manager_two = {222: 67, 566: 90}

print(manager_one)
print("____")
print(manager_two)
print("____")

manager_one.update(manager_two)
print(manager_one)