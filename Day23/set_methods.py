cities = {"Tokyo", "Madrid", "Berlin", "Karachi"}
cities2 = {"Tokyo", "Seoul", "Lahore", "Madrid"}
cities3 = cities.symmetric_difference(cities2) # returns non duplicate values
print(cities3)

print("_______")

cities = {"Tokyo", "Madrid", "Berlin", "Karachi"}
cities2 = {"Tokyo", "Seoul", "Lahore", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)

print("_______")

cities = {"Tokyo", "Madrid", "Berlin", "Karachi"}
cities2 = {"Tokyo", "Seoul", "Lahore", "Madrid"}
cities3 = cities.isdisjoint(cities2)
print(cities3)

print("_______")

cities = {"Tokyo", "Madrid", "Berlin", "Karachi"}
cities2 = {"Tokyo", "Seoul", "Lahore", "Madrid"}
cities3 = cities.issuperset(cities2)
print(cities3)

print("_______")

cities = {"Tokyo", "Madrid", "Berlin", "Karachi"}
cities2 = {"Tokyo", "Seoul", "Lahore", "Madrid"}
cities3 = cities.issuperset(cities2)
print(cities3)

print("_______")

cities = {"Tokyo", "Madrid", "Berlin", "Karachi"}
cities2 = {"Tokyo", "Seoul", "Lahore", "Madrid"}
cities3 = cities.issubset(cities2)
print(cities3)

print("_______")

cities = {"Tokyo", "Madrid", "Berlin", "Karachi"}
cities2 = {"Tokyo", "Seoul", "Lahore", "Madrid"}
cities.remove("Tokyo")
print(cities)

print("_______")

cities = {"Tokyo", "Madrid", "Berlin", "Karachi"}
cities2 = {"Tokyo", "Seoul", "Lahore", "Madrid"}
cities2.discard("Seoul")
print(cities2)

# print("_______")

# cities = {"Tokyo", "Madrid", "Berlin", "Karachi"}
# cities2 = {"Tokyo", "Seoul", "Lahore", "Madrid"}
# del cities
# print(cities)

print("_______")

cities = {"Tokyo", "Madrid", "Berlin", "Karachi"}
cities2 = {"Tokyo", "Seoul", "Lahore", "Madrid"}
cities.clear()
print(cities)