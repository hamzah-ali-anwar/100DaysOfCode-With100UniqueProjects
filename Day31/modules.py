# math - used for mathematical operations
import math

# random - for random number generation
import random

# datetime - for working with dates and times
from datetime import datetime

# os - interacting with operating system, reading file and environment variables
import os

# sys - access system-related functions and manipulate runtime env
import sys

#math
print(math.sqrt(25))
print(round(math.pi, 2))

#random
print(random.randint(1, 10))
print(random.choice(["apple", "banana", "cherry"]))

#datetime
now = datetime.now()

print(now)
print(now.strftime("%Y-%m-%d"))

#os
print(os.getcwd())
print(os.listdir())

#sys
print(sys.version)
sys.exit()