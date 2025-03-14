try:
    num = 42
    num.append(5) # Integers don't have an append method
except AttributeError:
    print("Erro: 'int' object has no attribute 'append'.")
