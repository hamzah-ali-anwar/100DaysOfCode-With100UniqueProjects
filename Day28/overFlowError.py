try:
    import math
    print(math.eth(1000))
except OverflowError:
    print("Error: Number too large")