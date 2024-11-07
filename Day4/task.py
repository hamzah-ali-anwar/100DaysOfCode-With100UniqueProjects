import random

randomIntegers = random.randint(1, 100)
print(randomIntegers)

random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)

# Toss
toss = random.randint(0, 1)
if toss == 0:
    print("Heads")
else:
    print("Tails")