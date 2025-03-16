def test():
    try:
        print(value)
    except UnboundLocalError:
        print("Error: variable is used before assignment")

test()