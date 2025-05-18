# Project # 06 Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# Created By Hassan Khan

# 5. Static Variables and Static Methods

# Assignment 5:

# Create a class MathUtils with a static method add(a, b) that returns the sum. 
# No class or instance variables should be used.

# SOLUTION:

class MathUtils:
    @staticmethod
    def add(a, b):
        # ➕ Static method for adding two numbers without needing an object
        return a + b

# 🚀 Example
print("\n 🧮 Welcome to Math Utils!")

# 🔢 Adding two numbers
result = MathUtils.add(4, 25)
print(f"\n ✅ The sum of 20 and 30 is: {result} 🎉")
print("\n 🔚 Thank you for using Math Utils!")

# --------------- ASSIGNMENT 5 END ---------------