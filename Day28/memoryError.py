try:
    huge_list = [1] * (10**10) # This may cause memory error
except MemoryError:
    print("Error: Not enough memory.")