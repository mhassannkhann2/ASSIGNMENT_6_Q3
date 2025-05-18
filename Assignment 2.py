# Project # 06 Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# Created By Hassan Khan

# 2. Using cls

# Assignment 2:

# Create a class Counter that keeps track of how many objects have been created. 
# Use a class variable and a class method with cls to manage and display the count.

# SOLUTION :

class Counter:
    count = 0  # 🔢 Class variable to keep track of the number of objects

    def __init__(self):
        Counter.count += 1  # ➕ Increment the counter when a new object is created
        print("\n ✨ Welcome! A new Counter object has been created.")

    @classmethod
    def display_count(cls):
        print("\n📊 Total objects created:", cls.count)

# Example usage
print("🎉 Let's start counting!")
c1 = Counter()
c2 = Counter()
c3 = Counter()
c4 = Counter()

Counter.display_count()

# ------------- Assignment 2 End -------------

