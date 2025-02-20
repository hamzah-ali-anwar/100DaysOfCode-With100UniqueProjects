# union method
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.union(s2)) # 1, 2, 3, 5, 6, 7

print("___________")

cities = {"Tokyo", "Madrid", "Berlin", "Karachi"}
cities2 = {"Tokyo", "Seoul", "Lahore", "Madrid"}
print(cities.union(cities2)) # Tokyo, Madrid, Berlin, Karachi, Seoul, Lahore

print("___________")

cities = {"Tokyo", "Madrid", "Berlin", "Karachi"}
cities2 = {"Tokyo", "Seoul", "Lahore", "Madrid"}
print(cities.intersection(cities2)) # Tokyo, Mardid

print("___________")

cities = {"Tokyo", "Madrid", "Berlin", "Karachi"}
cities2 = {"Tokyo", "Seoul", "Lahore", "Madrid"}
cities.update(cities2)
print(cities) # Tokyo, Madrid, Berlin, Karachi, Seoul, Lahore

print("___________")

cities = {"Tokyo", "Madrid", "Berlin", "Karachi"}
cities2 = {"Tokyo", "Seoul", "Lahore", "Madrid"}
cities.intersection_update(cities2)
print(cities) # Tokyo, Madrid

