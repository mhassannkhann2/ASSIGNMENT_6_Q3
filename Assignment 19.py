# Project # 06 Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# Created By Hassan Khan

# 19. callable() and __call__()

# Assignment 19 :

# Create a class Multiplier with an __init__() to set a factor. 
# Define a __call__() method that multiplies an input by the factor. 
# Test it with callable() and by calling the object like a function.

# SOLUTION:

# 👋 Welcome to the Python Callable Class Demonstration! 👋
# This program showcases how objects can be made callable using the __call__ method.

class Multiplier:
    def __init__(self, factor):
        """Initialize with a multiplication factor."""
        self.factor = factor  # Store the multiplication factor

    def __call__(self, number):
        return number * self.factor

# 🎉 Example

print("\n✖️  Welcome to the Python Callable Class Showcase! ✖️")
print("\nUse callable objects like functions for dynamic multiplications. 🚀\n")

# Create an instance of the callable Multiplier class
multiplier = Multiplier(7)

# Test if the object is callable using the built-in callable() function
print("🧐 Is 'multiplier' callable?")
print(callable(multiplier))  # Output: True

# Call the object like a function to perform multiplication
print("\n✅ Calling 'multiplier' instance with number 10:")
result = multiplier(10)  # Multiplies 10 by the factor (5)
print(f"\n🔢 Result of multiplying by factor: {result}")  # Output: 50

# ----------------- Assignment 19 Completed -----------------

