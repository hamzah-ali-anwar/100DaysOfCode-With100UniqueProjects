try:
    import nonexistent_module
except ImportError:
    print("Error: Module not found")