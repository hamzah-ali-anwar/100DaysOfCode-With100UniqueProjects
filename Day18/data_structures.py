# Data structures allows you to store and organize data efficiently for various operations
# Some most commonly used data structures

# List
lst = [1, 2, 3, 4]

accessFirstElement = lst[0]
print(accessFirstElement)

slicing = lst[1:3]
print(slicing)

addElementAtEnd = lst.append(5)
print(lst)

insertAtSpecificIndex = lst.insert(4, 10)
print(lst)

removeByValue = lst.remove(10)
print(lst)

print(len(lst))