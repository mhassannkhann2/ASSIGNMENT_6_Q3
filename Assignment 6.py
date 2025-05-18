# Project # 06 Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# Created By Hassan Khan

# 6. Constructors and Destructors

# Assignment 6:

# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

# SOLUTION:

class Logger:
    def __init__(self):
        # 📥 Constructor runs when object is created
        print("\n ✅ Logger initialized! Object created successfully. 🛠️")

    def __del__(self):
        # 🗑️ Destructor runs when object is deleted
        print("\n ⚠️  Logger destroyed! Object deleted from memory. 💨")

# 🚀 Example usage
print("\n 📦  Creating Logger object...")
logger1 = Logger()

# 🧹 Manually delete the object to trigger the destructor
print("\n 🗑️  Deleting Logger object...")
del logger1

# ----------------- ASSIGNMENT 6 END ---------------