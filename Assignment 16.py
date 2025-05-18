# Project # 06 Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# Created By Hassan Khan

# 16. Function Decorators

# Assignment 16 :

# Write a decorator function log_function_call that prints "Function is being called" before a function executes. 
# Apply it to a function say_hello().

# SOLUTION :

def log_function_call(func):
    """
    A decorator function that logs when a function is being called.
    
    It wraps the original function and adds an extra print statement
    before executing the function.
    """
    def wrapper():
        print("\n ⚡ Function is being called... ⚡")  # Log message
        return func()  # Call the original function
    return wrapper

# 🏷️ Applying the decorator to the say_hello function
@log_function_call
def say_hello():
    """
    A simple function that prints a friendly greeting.
    """
    print("\n 🌍 Hello, World! 🌟")

# 🎉 Example Usage 🎉
print("\n 🔧 Welcome to the Python Decorator Showcase! 🔧")
print("\n Enhance your functions dynamically with decorators. 🚀\n")

# Call the decorated function
print("\n ✅ Calling 'say_hello' function now:")
say_hello()  # Output: Logs the function call before executing it

# -------------- Assignemnt 16 Completed --------------