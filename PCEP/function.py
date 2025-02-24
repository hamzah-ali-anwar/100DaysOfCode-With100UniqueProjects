# For this practice challenge, write a simple greeter function.

# If it is passed in a name NAME, return "Hello, NAME!".
# If it is called without a name, return "Hello there!".

def say_hello(name: str = None) -> str:

    if name:
        return f"Hello, {name}!"
    else:
        return f"Hello, there!"
    
print(say_hello("Alice"))
print(say_hello())