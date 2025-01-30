data = ('Emma', 'Software Engineer', 'Python', 'AWS', 'SQL')

name, occupation, *skills = data

print(name)
print(occupation)
print(*skills)