try:
    import fake_module
except ModuleNotFoundError:
    print("Error: Module does not exist.")