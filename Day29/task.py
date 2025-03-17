salary = int(input("Enter your salary: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")
else:
    print(salary)